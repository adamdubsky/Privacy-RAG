# Privacy-RAG

Privacy-RAG is an offline Retrieval-Augmented Generation (RAG) backend
built for privacy sensitive domains such as accounting and finance.  It
uses **FastAPI** for the web interface, **llama.cpp** for running a local
large language model, **bge-m3** embeddings and **ChromaDB** for vector
storage.  The project performs all processing locally with no external
API calls.

## Features

- Upload encrypted PDF or Excel files
- Parse and chunk documents into manageable pieces
- Generate embeddings for each chunk using a local model
- Persist embeddings in a local ChromaDB vector store
- Query the documents via a chat style API backed by a local LLM

## Directory Structure

```
server/               Backend code
├── main.py           FastAPI application
├── ask.py            Simple CLI for questions
├── routers/          API route definitions
└── services/         Parsing, chunking, embedding and storage utilities
```

## Installation

1. Install Python 3.10 or newer.
2. Clone this repository and install the requirements:

   ```bash
   pip install -r requirements.txt
   ```
3. Provide a local Llama model path by editing `.env` or setting the
   environment variable `LLAMA_MODEL_PATH`.

## Running the API

Start the development server with **uvicorn**:

```bash
uvicorn server.main:app --reload
```

The interactive documentation is available at `http://localhost:8000/docs`.

### CLI Usage

A small command line helper is included for quick experiments:

```bash
python server/ask.py
```

You will be prompted for a question and the answer will be generated using
the local model and document context.

## Security Notes

Uploaded files are encrypted with a symmetric key before being stored on
disk.  The key is hard coded for development purposes and should be
replaced with a secure key management solution for production deployments.

## Contributing

Pull requests are welcome!  Feel free to open issues or suggest
improvements.

## License

This project is released under the MIT License.
