import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("LLm_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not LLm_API_KEY:
    print("WARNING: GROQ_API_KEY not found in environment variables or .env file.")
    print("Please create a .env file in the same directory with LLM_API_KEY=\"your_key\"")
    exit()

if not GOOGLE_API_KEY:
    print("WARNING: GOOGLE_API_KEY not found in environment variables or .env file.")
    print("Please create a .env file in the same directory with GOOGLE_API_KEY=\"your_key\"")
    print("This is used for embeddings. You can get an API key from Google AI Studio: https://aistudio.google.com/app/apikey")
    exit()

pdf_file_path = "your_document.pdf"

if not os.path.exists(pdf_file_path):
    print(f"Creating a dummy PDF file '{pdf_file_path}' for demonstration.")
    dummy_content = """
    This is a dummy PDF content.
    LangChain is a powerful framework for building LLM applications.
    RAG systems enhance LLMs with external knowledge.
    Groq provides fast inference for large language models.
    """
    with open(pdf_file_path, "w") as f:
        f.write(dummy_content)
    print(f"Please replace '{pdf_file_path}' with your actual PDF file for proper functionality.")

print(f"Loading document from {pdf_file_path}...")
try:
    loader = PyPDFLoader(pdf_file_path)
    documents = loader.load()
    print(f"Loaded {len(documents)} page(s) from PDF.")
except Exception as e:
    print(f"Error loading PDF: {e}")
    print("Please ensure 'pypdf' is installed (pip install pypdf) and the PDF file path is correct and accessible.")
    exit()

print("Splitting document into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)
print(f"Split into {len(chunks)} chunks.")

print("Creating embeddings and building vector store (ChromaDB)...")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
vector_store = Chroma.from_documents(chunks, embeddings)
print("Vector store created.")

retriever = vector_store.as_retriever()

print("Initializing LLM...")
llm = ChatGroq(model="llama3-80b-8192", groq_api_key=LLm_API_KEY)
print("LLM initialized.")

prompt = ChatPromptTemplate.from_template("""
Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}
""")

document_chain = create_stuff_documents_chain(llm, prompt)

retrieval_chain = create_retrieval_chain(retriever, document_chain)
print("RAG chain created.")

print("\n--- Enter your questions below (type 'exit' to quit) ---")

while True:
    user_question = input("\nYour Question: ")
    if user_question.lower() == 'exit':
        break

    try:
        response = retrieval_chain.invoke({"input": user_question})
        print(f"Answer: {response['answer']}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your Groq API Key is valid and has access to the specified model.")

if os.path.exists(pdf_file_path) and "This is a dummy PDF content" in open(pdf_file_path, "r").read():
    os.remove(pdf_file_path)
