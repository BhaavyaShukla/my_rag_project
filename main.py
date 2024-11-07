from fastapi import FastAPI, UploadFile, File, HTTPException
from sentence_transformers import SentenceTransformer
from typing import List
import chromadb
from chromadb.config import Settings

app = FastAPI()

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

persist_directory = "/Users/bhavyashukla/my_rag_project/data"
chroma_client = chromadb.Client(Settings(persist_directory=persist_directory))

@app.post("/ingest")
async def ingest_document(files: List[UploadFile] = File(...)):
    
    for file in files:
        content = await file.read()  # Read the file content
        text = content.decode("utf-8")  # Decode file content to text
        embedding = model.encode(text).tolist()  # Get embedding of the text

        chroma_client.add_documents(texts=[text], embeddings=[embedding])

    return {"status": "Documents ingested successfully"}

@app.get("/query")
async def query_document(query: str):
   
    query_embedding = model.encode(query).tolist()
    results = chroma_client.query(query_embeddings=[query_embedding], n_results=3)  # Query similar documents

    if not results:
        raise HTTPException(status_code=404, detail="No similar documents found")

    return {"results": results}