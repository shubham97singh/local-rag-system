import glob
import os

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ==========================================================
# Configuration
# ==========================================================

BOOKS_DIR = "books"

CHROMA_DB = "chroma_db"

COLLECTION_NAME = "books"

EMBEDDING_MODEL = "mxbai-embed-large"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 5

BATCH_SIZE = 50

# ==========================================================
# Embedding Model
# ==========================================================

embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL
)

# ==========================================================
# Vector Store
# ==========================================================

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=CHROMA_DB,
    embedding_function=embeddings
)

# ==========================================================
# Check if Vector DB already contains documents
# ==========================================================

collection = vector_store.get()

if len(collection["ids"]) == 0:

    print("=" * 60)
    print("Building Vector Database")
    print("=" * 60)

    pdf_files = glob.glob(
        os.path.join(BOOKS_DIR, "*.pdf")
    )

    if len(pdf_files) == 0:
        raise Exception(
            "No PDF files found inside the books folder."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    documents = []

    # ======================================================
    # Read every PDF
    # ======================================================

    for pdf in pdf_files:

        filename = os.path.basename(pdf)

        print(f"\nLoading {filename}")

        loader = PyPDFLoader(pdf)

        pages = loader.load()

        chunks = splitter.split_documents(pages)

        for chunk in chunks:

            text = chunk.page_content.strip()

            if len(text) == 0:
                continue

            chunk.metadata["source"] = filename

            documents.append(chunk)

    print("\n")
    print("=" * 60)
    print(f"Total Chunks : {len(documents)}")
    print("=" * 60)

    # ======================================================
    # Test embedding before indexing thousands of chunks
    # ======================================================

    print("\nTesting embedding model...")

    embeddings.embed_query(documents[0].page_content)

    print("Embedding model working.\n")

    # ======================================================
    # Index in batches
    # ======================================================

    total = len(documents)

    for start in range(0, total, BATCH_SIZE):

        end = min(start + BATCH_SIZE, total)

        batch = documents[start:end]

        try:

            vector_store.add_documents(batch)

            print(
                f"Indexed {end}/{total}"
            )

        except Exception as e:

            print("\nError while indexing batch")

            print(f"Start : {start}")

            print(f"End   : {end}")

            print(e)

            raise

    print("\nVector Database Created Successfully!")

else:

    print("=" * 60)
    print("Existing Vector Database Found")
    print("=" * 60)
    print(f"Indexed Documents : {len(collection['ids'])}")

# ==========================================================
# Retriever
# ==========================================================

retriever = vector_store.as_retriever(
    search_kwargs={
        "k": TOP_K
    }
)