# Retrieval-Augmented Generation (RAG) with LangChain and PDF Support

This project implements a basic Retrieval-Augmented Generation (RAG) system using the LangChain framework. It leverages a fast Large Language Model (LLM) inference and Google Generative AI for embeddings, allowing you to query information based on content extracted from a PDF document.

## 🌟 Features

* **PDF Document Ingestion:** Loads and processes content directly from a PDF file.
* **Text Chunking:** Splits large documents into smaller, manageable chunks for efficient retrieval.
* **Vector Database (ChromaDB):** Stores document embeddings for semantic search.
* **LLM Integration:** Utilizes a high-speed Language Processing Unit (LPU) for rapid LLM inference.
* **Google Generative AI Embeddings:** Generates high-quality embeddings for document chunks.
* **Interactive Q&A:** Allows users to ask questions via the terminal and receive answers grounded in the PDF content.
* **Environment Variable Support:** Securely loads API keys from a `.env` file.

## 🚀 Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**
* **pip** (Python package installer)
* **Git** (for cloning the repository, if applicable)
* **An LLM API Key:** Obtain one from your chosen LLM provider .
* **A Google Generative AI API Key:** Obtain one from [Google AI Studio](https://aistudio.google.com/app/apikey).

## 🛠️ Setup

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository (Optional, if you have the files locally)

If you have already created the files locally, you can skip this step. Otherwise:

```bash
git clone <your-repository-url>
cd <your-project-directory>
