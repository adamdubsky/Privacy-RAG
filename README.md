# Privacy-RAG


A fully local, secure Retrieval-Augmented Generation (RAG) system designed for accounting and financial services. Built using FastAPI, local LLMs (via llama.cpp), local embeddings (bge-m3), and ChromaDB — with zero external API calls.

## Overview

This system:
- Accepts PDF and Excel files
- Parses and chunks documents locally
- Embeds content with a local model
- Stores embeddings in a local vector database (Chroma)
- Answers natural language questions using a local LLM

All processing is done entirely offline, making it ideal for privacy-sensitive domains like accounting, legal, and finance.

## Core Features (Work in Progress)

- Local file upload (PDF/Excel)
- Chunked parsing and storage
- FastAPI backend with `/upload` and `/chat` routes
- All data handled and stored securely, locally

## Hopeful Features (Planned)

- Chunk-level access control (per user/team)
- PDF viewer with highlightable citations
- LLM reasoning trace (“train of thought”) in output
- Sensitive info redaction
- User memory and session history
- Full audit logging
- Dockerized deployment (backend and frontend)
- Simple Vue-based frontend (chat and file upload)

## Contact

For questions, feedback, or collaboration, contact:  
**adamdubsky@gmail.com**
