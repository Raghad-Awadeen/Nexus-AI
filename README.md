# Nexus AI – Enterprise Knowledge Assistant

Nexus AI is an AI-powered Enterprise Knowledge Assistant that allows users to upload PDF documents and ask questions about their content using Retrieval-Augmented Generation (RAG).

The system retrieves relevant document passages using semantic search and generates context-grounded answers using a Large Language Model (LLM).

## Features

- PDF document processing and text extraction.
- Text chunking with configurable chunk size and overlap.
- Semantic embeddings using Voyage AI.
- Semantic search to retrieve relevant document passages.
- AI-generated answers using Groq.
- Source-based answers with retrieved document excerpts.
- FastAPI backend with health-check endpoints.
- Streamlit user interface.

## Tech Stack

- Python 3.11
- FastAPI
- Streamlit
- Voyage AI
- Groq API
- PyMuPDF
- Requests

## Project Structure

```text
nexus-ai/
│
├── backend/
│   ├── answer_generator.py
│   ├── document_pipeline.py
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── knowledge_base.py
│   ├── main.py
│   ├── semantic_search.py
│   └── text_chunker.py
│
├── frontend/
│   └── app.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd nexus-ai
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
VOYAGE_API_KEY=your_voyage_api_key
GROQ_API_KEY=your_groq_api_key
```

Never commit your actual API keys.

## Running the Application

Start the FastAPI backend:

```bash
uvicorn backend.main:app --reload
```

Start the Streamlit frontend in a separate terminal:

```bash
streamlit run frontend/app.py
```

Open the application using the local URL provided by Streamlit.

## How It Works

1. Upload a PDF document.
2. Extract and split its text into smaller chunks.
3. Generate embeddings using Voyage AI.
4. Retrieve relevant passages using semantic search.
5. Send the retrieved context and user question to Groq.
6. Generate an answer grounded in the document content.

## Project Status

Prototype v0.1 – Core document processing, semantic retrieval, and AI-powered question answering are implemented.

## Author

Developed as a practical project exploring LLM applications and Retrieval-Augmented Generation (RAG).