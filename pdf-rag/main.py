from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from vector import retriever

llm = OllamaLLM(
    model="llama3.2"
)

template = """
You are an expert AI assistant.

Answer ONLY using the provided context.

If the answer is not contained in the context,
reply:

"I could not find that information in the provided books."

Context:

{context}

Question:

{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | llm

while True:

    print("\n" + "=" * 70)

    question = input("Ask a question (q to quit): ")

    if question.lower() == "q":
        break

    docs = retriever.invoke(question)

    context = ""

    print("\nRelevant Sources\n")

    for doc in docs:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "Unknown"
        )

        print(f"{source} | Page {page}")

        context += doc.page_content
        context += "\n\n"

    print("\nGenerating answer...\n")

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    print(answer)