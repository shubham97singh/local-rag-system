# 🚀 Quick Start & Setup Guide

Follow the steps below to run this **Local AI Agent** on your machine.

> **Everything runs 100% locally.** No cloud APIs, API keys, or paid subscriptions are required.

---

## 📋 Prerequisites

Before getting started, install **Ollama**, which allows you to run Large Language Models (LLMs) locally.

Download and install Ollama from:

**https://ollama.com**

After installation, verify it is working:

```bash
ollama --version
```

---

# Step 1: Download the Required AI Models

This project uses two Ollama models:

* **Llama 3.2** – Large Language Model used for generating responses.
* **mxbai-embed-large** – Embedding model used to convert text into vectors for semantic search.

Download the models using the following commands:

### Download Llama 3.2

```bash
ollama pull llama3.2
```

### Download the Embedding Model

```bash
ollama pull mxbai-embed-large
```

> **Note:** The downloads may take a few minutes depending on your internet speed.

You can verify the installed models with:

```bash
ollama list
```

---

# Step 2: Create a Python Virtual Environment

Using a virtual environment keeps the project's dependencies isolated from your global Python installation.

### Create the virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

#### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

#### Windows (Command Prompt)

```cmd
venv\Scripts\activate.bat
```

#### macOS / Linux

```bash
source venv/bin/activate
```

Once activated, your terminal should display:

```text
(venv)
```

---

# Step 3: Install Python Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This installs libraries such as:

* LangChain
* LangChain Ollama
* LangChain Chroma
* ChromaDB
* Pandas
* Ollama Python SDK
* Other required dependencies

---

# Step 4: Run the Application

Start the AI Agent by running:

```bash
python main.py
```

On the first run, the application will:

1. Load the restaurant reviews from the CSV file.
2. Generate embeddings using **mxbai-embed-large**.
3. Create a Chroma vector database.
4. Store the embedded documents.
5. Launch the AI agent.

On subsequent runs, the existing Chroma database will be reused automatically.

---

# 📁 Project Structure

```text
.
├── main.py
├── vector.py
├── realistic_restaurant_reviews.csv
├── requirements.txt
├── chroma_langchain_db/
└── README.md
```

---

# 🛠 Technologies Used

* Python
* Ollama
* LangChain
* LangChain Ollama
* LangChain Chroma
* ChromaDB
* Pandas

---

# 💡 How It Works

```text
Restaurant Reviews (CSV)
           │
           ▼
Read with Pandas
           │
           ▼
Create LangChain Documents
           │
           ▼
Generate Embeddings
(mxbai-embed-large)
           │
           ▼
Store in Chroma Vector Database
           │
           ▼
User Question
           │
           ▼
Retriever Finds Relevant Reviews
           │
           ▼
Llama 3.2 Generates Response
```

---

# ✅ You're Ready!

Your local AI Agent is now ready to answer questions about the restaurant reviews using Retrieval-Augmented Generation (RAG), LangChain, Ollama, and ChromaDB.