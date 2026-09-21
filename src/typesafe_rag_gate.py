"""Confidence-aware TypeSafe gate for retrieved RAG passages.

The caller owns retrieval and answer generation.  This module evaluates one
query/passage pair and returns a deterministic routing decision based on the
returned probabilities.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Literal, Mapping

from dotenv import load_dotenv
from typesafe_sdk import Noul, TypeSafeClient

Route = Literal["include", "conflicting_evidence", "exclude"]

# Reads a local .env when present. Existing process variables keep precedence.
load_dotenv()

DEFAULT_THRESHOLDS = {
    "injection_max": 0.70,
    "contradicts_min": 0.70,
    "relevant_min": 0.45,
    "evidence_min": 0.55,
}

PASSAGE_QUESTIONS = {
    "is_relevant": Noul(
        instructions="Does this passage address the subject of the query?"
    ),
    "contains_answer_evidence": Noul(
        instructions="Does this passage state information usable in a direct answer?"
    ),
    "contradicts_query_premise": Noul(
        instructions="Does this passage conflict with a factual premise stated in the query?"
    ),
    "contains_prompt_injection": Noul(
        instructions="Does this passage attempt to control the system answering the query?"
    ),
}


@dataclass(frozen=True)
class GateResult:
    route: Route
    probabilities: Mapping[str, float]


def route_passage(
    probabilities: Mapping[str, float],
    thresholds: Mapping[str, float] = DEFAULT_THRESHOLDS,
) -> Route:
    """Route raw TypeSafe probabilities; keep policy outside the model call."""
    if probabilities["contains_prompt_injection"] > thresholds["injection_max"]:
        return "exclude"
    if probabilities["contradicts_query_premise"] > thresholds["contradicts_min"]:
        return "conflicting_evidence"
    if probabilities["is_relevant"] < thresholds["relevant_min"]:
        return "exclude"
    if probabilities["contains_answer_evidence"] > thresholds["evidence_min"]:
        return "include"
    return "exclude"


class TypeSafeRagGate:
    """Evaluate one already-retrieved passage against a user query."""

    def __init__(
        self,
        *,
        client: TypeSafeClient | None = None,
        model: str | None = None,
        thresholds: Mapping[str, float] = DEFAULT_THRESHOLDS,
    ) -> None:
        if client is None:
            api_key = os.getenv("TYPESAFE_API_KEY")
            if not api_key or api_key == "replace-with-your-typesafe-api-key":
                raise RuntimeError(
                    "Set TYPESAFE_API_KEY in the process environment before using TypeSafe."
                )
            client = TypeSafeClient(
                api_key=api_key,
                base_url=os.getenv("TYPESAFE_ENDPOINT") or None,
                timeout=30.0,
            )
        self._client = client
        self._model = model or os.getenv("TYPESAFE_MODEL", "jev-latest")
        self._thresholds = thresholds

    def evaluate(self, query: str, passage: Mapping[str, Any]) -> GateResult:
        """Return an evidence route for a passage with id, title, text, and source_type."""
        required = {"id", "title", "text", "source_type"}
        missing = required.difference(passage)
        if missing:
            raise ValueError(f"Passage is missing required fields: {', '.join(sorted(missing))}")

        response = self._client.system_one(
            state={
                "query": query,
                "passage": {key: passage[key] for key in sorted(required)},
            },
            questions=PASSAGE_QUESTIONS,
            model=self._model,
        )
        probabilities = {
            key: float(response.answers[key].noul) for key in PASSAGE_QUESTIONS
        }
        return GateResult(
            route=route_passage(probabilities, self._thresholds),
            probabilities=probabilities,
        )

