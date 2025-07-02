Retrieval-Augmented Generation (RAG) with LangChain and PDF Support
This project implements a basic Retrieval-Augmented Generation (RAG) system using the LangChain framework. It leverages a fast Large Language Model (LLM) inference and Google Generative AI for embeddings, allowing you to query information based on content extracted from a PDF document.

🌟 Features
PDF Document Ingestion: Loads and processes content directly from a PDF file.

Text Chunking: Splits large documents into smaller, manageable chunks for efficient retrieval.

Vector Database (ChromaDB): Stores document embeddings for semantic search.

LLM Integration: Utilizes a high-speed Language Processing Unit (LPU) for rapid LLM inference.

Google Generative AI Embeddings: Generates high-quality embeddings for document chunks.

Interactive Q&A: Allows users to ask questions via the terminal and receive answers grounded in the PDF content.

Environment Variable Support: Securely loads API keys from a .env file.

🚀 Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8+

pip (Python package installer)

Git (for cloning the repository, if applicable)

An LLM API Key: Obtain one from your chosen LLM provider (e.g., Groq Console).

A Google Generative AI API Key: Obtain one from Google AI Studio.

🛠️ Setup
Follow these steps to get the project up and running on your local machine.

1. Clone the Repository (Optional, if you have the files locally)
If you have already created the files locally, you can skip this step. Otherwise:

git clone <your-repository-url>
cd <your-project-directory>


2. Install Dependencies
Navigate to your project directory in the terminal and install the required Python libraries:

pip install langchain langchain-groq langchain-google-genai pypdf python-dotenv chromadb


3. API Key Configuration
Create a file named .env in the root directory of your project (the same directory where your Python script is located). Add your API keys to this file as follows:

LLM_API_KEY="your_actual_llm_api_key"
GOOGLE_API_KEY="your_actual_google_api_key"


Important: Replace "your_actual_llm_api_key" and "your_actual_google_api_key" with your actual keys. Do not share your .env file or commit it to version control (e.g., add .env to your .gitignore).

4. Place Your PDF Document
Place the PDF file you want to use for question answering in the same directory as your Python script. Rename it to your_document.pdf or update the pdf_file_path variable in the script to point to your PDF's actual name/path.

# In your Python script (e.g., `rag_app.py`)
pdf_file_path = "your_document.pdf" # Make sure this matches your PDF file name


🏃 Usage
Once set up, you can run the RAG system and start asking questions.

Run the Python Script:

python your_script_name.py


(Replace your_script_name.py with the actual name of your Python file, e.g., rag_qa.py).

Interact in the Terminal:
The script will load the PDF, process it, and then prompt you to enter questions.

Loading document from your_document.pdf...
Loaded X page(s) from PDF.
Splitting document into chunks...
Split into Y chunks.
Creating embeddings and building vector store (ChromaDB)...
Vector store created.
Initializing LLM...
LLM initialized.
RAG chain created.

--- Enter your questions below (type 'exit' to quit) ---

Your Question: What is LangChain?
Answer: LangChain is a framework designed to simplify the creation of applications using large language models.

Your Question: What is this project known for?
Answer: This project is known for building LPU (Language Processing Unit) inference engines for AI workloads, offering extremely fast inference for large language models.

Your Question: exit


⚙️ Customization
LLM Model: You can change the LLM model used by modifying the model parameter in ChatGroq (e.g., model="llama3-70b-8192").

Embedding Model: If you wish to use a different embedding model, you would replace GoogleGenerativeAIEmbeddings with another LangChain-supported embedding class.

Chunking Strategy: Adjust chunk_size and chunk_overlap in RecursiveCharacterTextSplitter to fine-tune how your document is broken down.

Vector Store: For larger applications, consider persistent ChromaDB or other vector databases like Pinecone, Weaviate, or FAISS.

Prompt Engineering: Experiment with the ChatPromptTemplate to guide the LLM's responses more effectively.

📄 License
This project is open-source and available under the MIT License
