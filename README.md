# 🧠 DocuQuery – AI-Powered Document Q&A API

DocuQuery is a FastAPI-based backend that allows users to upload documents (PDF or TXT) and ask natural language questions about their contents. It uses **Mistral (via Ollama)** for language understanding, **FAISS** for vector search, and integrates with **MongoDB** and **Redis** for storage, logging, and performance.

Built to showcase real-world RAG (Retrieval-Augmented Generation) pipelines, this project demonstrates production-style AI backend engineering using modern tools and clean architecture.

---

## 🚀 Features

- 📄 Upload PDF or TXT documents via API
- 🧠 Ask questions based on document content (RAG)
- ⚙️ Mistral LLM via [Ollama](https://ollama.com/)
- 📦 Vector search using FAISS
- 🛢️ MongoDB for metadata and logs
- 🧰 Redis for caching & rate limiting
- 🔐 Environment config via `.env`
- 📚 Built-in Swagger API docs (`/docs`)

---

## 🛠️ Tech Stack

| Layer            | Tools Used                    |
|------------------|-------------------------------|
| Backend API      | FastAPI, Pydantic             |
| Language Model   | Mistral via Ollama (local LLM)|
| Embeddings/RAG   | LangChain, FAISS              |
| File Parsing     | PDFPlumber, PyMuPDF           |
| Database         | MongoDB                       |
| Caching          | Redis                         |
| DevOps           | Uvicorn, dotenv               |

---

