# Security notes

This repository contains a local RAG proof of concept. Treat the source card,
PDF, Chroma database, and derived embeddings as private company data.

## Rules

- Never commit `.env`, API keys, passwords, access tokens, or private key files.
- Keep the GitHub repository private. Repository visibility is part of the data
  access boundary; changing it to public requires an explicit review.
- Keep `TYPESAFE_API_KEY` in a secret manager or process environment. If it is
  ever exposed, revoke it and issue a replacement before continuing.
- The Chroma database contains derived embeddings and document metadata. Share
  it only with authorized users and back it up as a versioned data artefact.
- Apply document-level authorization before retrieval in any production RAG
  service; vector similarity is not an access-control mechanism.
- Do not treat presentation claims as independently verified facts. Preserve the
  source and page metadata when returning an answer.

The upload set intentionally excludes `.env`, virtual environments, Python
bytecode, caches, and credential material. No Neo4j graph data is included when
the graph contains no verified nodes or relationships.

