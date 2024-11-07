
# My RAG Project

This project implements a lightweight FastAPI server for Retrieval-Augmented Generation (RAG), using ChromaDB for document storage and sentence-transformers for embeddings. The API supports document ingestion, querying, and retrieval using natural language processing models.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Usage Instructions](#usage-instructions)
6. [API Endpoints](#api-endpoints)
7. [Example Postman Requests](#example-postman-requests)
8. [Project Structure](#project-structure)
9. [Troubleshooting](#troubleshooting)

## Project Overview

The purpose of this project is to create a FastAPI server that can handle document ingestion and querying for RAG. By using ChromaDB with sentence-transformers, the server can efficiently manage and query document embeddings, supporting tasks that require high-speed, vectorized document retrieval.

## Features

- **Document Ingestion**: Upload documents in various formats (PDF, DOC, DOCX, TXT) and store embeddings in ChromaDB for efficient querying.
- **Natural Language Queries**: Use embeddings to search documents based on semantic similarity.
- **Persistent Storage**: Configure ChromaDB for persistent storage, allowing data to be retained across sessions.
- **Scalable API**: Built with FastAPI for lightweight, scalable, and asynchronous processing.

## Technologies Used

- **Python** (v3.12)
- **FastAPI** - Web framework for building APIs
- **Uvicorn** - ASGI server for FastAPI
- **ChromaDB** - Database for storing and querying document embeddings
- **sentence-transformers** - Pre-trained embeddings model (`all-MiniLM-L6-v2`)
- **Docker** (optional for containerization)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd my_rag_project
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up ChromaDB Storage Path**
   - Create a directory for ChromaDB’s persistent storage:
     ```bash
     mkdir -p /path/to/your/storage
     ```
   - Update `main.py` with your storage path:
     ```python
     from chromadb import Client
     from chromadb.config import Settings
     
     # Configure the ChromaDB client
     chroma_client = Client(Settings(persist_directory="/path/to/your/storage"))
     ```

5. **Run the Server**
   ```bash
   uvicorn app.main:app --reload
   ```
   The server will be running at `http://127.0.0.1:8000`.

## Usage Instructions

To interact with the API, you can use [Postman](https://www.postman.com/downloads/) or `curl` commands. Set up a new collection in Postman and add requests for each endpoint. Be sure to update the base URL and tokens where necessary.

## API Endpoints

### 1. **Upload Document**
   - **Endpoint**: `POST /upload`
   - **Description**: Ingest a document for storage and embedding.
   - **Parameters**: Document file (PDF, DOC, DOCX, TXT)
   - **Example Request** (in Postman):
     ```http
     POST http://127.0.0.1:8000/upload
     ```
   - **Example Response**:
     ```json
     {
       "status": "Document uploaded successfully",
       "document_id": "12345"
     }
     ```

### 2. **Query Document**
   - **Endpoint**: `POST /query`
   - **Description**: Retrieve documents matching a natural language query.
   - **Parameters**:
     - `query`: The text query.
   - **Example Request**:
     ```http
     POST http://127.0.0.1:8000/query
     {
       "query": "Find documents about AI applications."
     }
     ```
   - **Example Response**:
     ```json
     {
       "matches": [
         {"document_id": "12345", "content": "AI applications in healthcare..."},
         {"document_id": "67890", "content": "AI in renewable energy..."}
       ]
     }
     ```

## Example Postman Requests

1. **Base URL and Variables**:
   - In Postman, set `{{baseUrl}}` to `http://127.0.0.1:8000` and configure any required authentication tokens.
  
2. **Requests**:
   - Set up a `POST` request for each endpoint, using the examples above.

## Project Structure

```plaintext
my_rag_project/
│
├── app/
│   └── main.py                  # Main FastAPI application
│
├── data/                        # Directory for ChromaDB storage
│
├── .venv/                       # Virtual environment
│
├── requirements.txt             # Project dependencies
│
└── README.md                    # Project documentation
```

## Troubleshooting

- **Database Not Persisting**: Verify that the `persist_directory` is set correctly in `main.py` and has write permissions.
- **Dependencies**: If you experience issues with dependencies, try re-installing with:
  ```bash
  pip install -r requirements.txt
  ```
- **Server Issues**: Ensure that the `uvicorn` server is running and accessible at the base URL.

