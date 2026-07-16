# 📚 Local PDF RAG using LangChain, Ollama & ChromaDB

A fully local **Retrieval-Augmented Generation (RAG)** application that allows you to chat with your own PDF documents using **LangChain**, **Ollama**, and **ChromaDB**.

No OpenAI API key, cloud services, or paid subscriptions are required. Everything runs entirely on your machine.

---

# ✨ Features

* 📄 Read all PDF files from a `books/` folder automatically.
* 🧠 Generate embeddings using **mxbai-embed-large**.
* 🗂 Store embeddings in a persistent **ChromaDB** vector database.
* 🔍 Retrieve the most relevant document chunks using semantic search.
* 🤖 Generate answers using **Llama 3.2** running locally through Ollama.
* 📚 Display the source PDF and page number for retrieved context.
* 💾 Reuse the existing vector database on subsequent runs.
* ⚡ Batch indexing for improved performance.

---

# 🏗 Project Architecture

```text
                  +------------------+
                  |   PDF Books      |
                  |   books/*.pdf    |
                  +---------+--------+
                            |
                            ▼
                  PyPDFLoader
                            |
                            ▼
          RecursiveCharacterTextSplitter
                            |
                            ▼
                 LangChain Documents
                            |
                            ▼
          Ollama Embeddings (mxbai-embed-large)
                            |
                            ▼
                Chroma Vector Database
                            |
             User Question
                            |
                            ▼
                  Embed Question
                            |
                            ▼
              Chroma Similarity Search
                            |
                            ▼
             Top-K Relevant Chunks
                            |
                            ▼
               Prompt Construction
                            |
                            ▼
              Llama 3.2 (Ollama)
                            |
                            ▼
                  Final Answer
```

---

# 📁 Project Structure

```text
PDF-RAG/
│
├── books/
│   ├── Book1.pdf
│   ├── Book2.pdf
│   └── ...
│
├── chroma_db/
│
├── main.py
├── vector.py
├── requirements.txt
└── README.md
```

---

# 📋 Prerequisites

Install **Ollama** from:

https://ollama.com

Verify the installation:

```bash
ollama --version
```

---

# Step 1 – Download Required Models

### Llama 3.2

```bash
ollama pull llama3.2
```

### Embedding Model

```bash
ollama pull mxbai-embed-large
```

Verify the installed models:

```bash
ollama list
```

---

# Step 2 – Create a Virtual Environment

```bash
python -m venv venv
```

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks execution:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Windows CMD

```cmd
venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# Step 3 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 4 – Add Your Books

Place every PDF inside the **books** folder.

Example:

```text
books/
    Clean Code.pdf
    Spark Guide.pdf
    Python.pdf
    Databricks.pdf
```

The application automatically indexes every PDF in this folder.

---

# Step 5 – Run the Application

```bash
python main.py
```

---

# First Run

On the first execution the application will:

1. Scan the `books/` directory.
2. Load every PDF.
3. Split documents into chunks.
4. Generate embeddings.
5. Create the Chroma vector database.
6. Store all vectors.
7. Launch the chatbot.

---

# Subsequent Runs

If the vector database already exists, it will be reused instead of rebuilding the index.

If you add, remove, or modify PDFs, delete the `chroma_db` folder and run the application again to rebuild the index.

---

# Example Questions

* Explain Spark DataFrames.
* What is Retrieval-Augmented Generation?
* Summarize Chapter 5.
* What is Lazy Evaluation?
* Explain Delta Lake.
* Compare DataFrames and RDDs.
* How does LangChain work?
* What is cosine similarity?

---

# 🧠 Technologies Used

* Python
* LangChain
* LangChain Community
* LangChain Chroma
* LangChain Ollama
* ChromaDB
* Ollama
* PyPDF
* RecursiveCharacterTextSplitter

---

# 📚 Bonus Learning Resource

This project includes a bonus PDF guide:

**`pdf_rag_complete_guide.pdf`**

This guide explains:

* Retrieval-Augmented Generation (RAG)
* LangChain fundamentals
* Ollama
* Embeddings
* Vector databases
* ChromaDB
* Chunking
* Metadata
* Semantic search
* Prompt engineering
* Complete project workflow
* Production RAG architecture
* Common errors
* Interview preparation

### Learn by Chatting with the Documentation

You can copy the guide into the `books/` folder and rebuild the vector database.

The AI will then be able to answer questions such as:

* How does RAG work?
* What are embeddings?
* Explain ChromaDB.
* Why is chunking required?
* How does semantic search work?
* Explain the complete project architecture.

Your application effectively becomes its own interactive textbook.

---

# 🚀 Future Improvements

* Incremental indexing
* File hashing
* Automatic synchronization
* OCR for scanned PDFs
* Hybrid search
* Metadata filtering
* Source citations
* Conversation memory
* Streamlit UI
* Multi-format document support (DOCX, TXT, HTML, Markdown)

---

# 📄 License

This project is intended for learning and educational purposes.

---

# 👨‍💻 Author

**Shubham Singh**

If you found this project helpful, consider giving it a ⭐ on GitHub.
