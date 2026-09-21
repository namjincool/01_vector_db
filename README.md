# Hue Keynote RAG

## TypeSafe API setup

1. Create a key in the [TypeSafe console](https://console.typesafe.ai/).
2. Copy `.env.example` to `.env` and replace `TYPESAFE_API_KEY` locally. Never commit it.
3. Install the SDK into the current user Python:

   ```powershell
   py -m pip install --user -r requirements.txt
   ```

   This workspace path contains Korean characters; on the current Python build,
   `py -m venv .venv` fails during `ensurepip`. Use a virtual environment rooted
   at an ASCII-only path if isolation is required.

4. Use `TypeSafeRagGate` after your retriever returns candidates. It labels each
   passage as `include`, `conflicting_evidence`, or `exclude`; pass the first two
   categories to the answer model in separate evidence blocks.

```python
from src.typesafe_rag_gate import TypeSafeRagGate

gate = TypeSafeRagGate()
result = gate.evaluate(
    "What makes a completion claim trustworthy?",
    {
        "id": "hue-12",
        "title": "Completion is not evidence",
        "text": "A completion declaration is not operational evidence.",
        "source_type": "keynote",
    },
)
print(result.route, result.probabilities)
```

The thresholds in `src/typesafe_rag_gate.py` are initial values from the TypeSafe
RAG cookbook. Calibrate them against this corpus before making automated decisions.

`TYPESAFE_MODEL` defaults to `jev-latest`, TypeSafe's stable Jev alias. Pin a
versioned model ID only after calibrating these thresholds against a specific release.

### Promote `.env` settings to this Windows user's global environment

After replacing the placeholder key in `.env`, run:

```powershell
.\scripts\Set-TypeSafeUserEnv.ps1
```

The script rejects an empty or placeholder key, stores the real key and model in the
current Windows user's persistent environment, and never prints the key. Open a new
terminal (or restart the app) afterwards. This makes TypeSafe available to future local
Python processes without copying the key into each project; it does not configure other
Windows accounts or remote deployments.

