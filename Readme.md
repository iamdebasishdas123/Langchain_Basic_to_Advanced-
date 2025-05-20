
# LangChain: Basic to Advanced

## Introduction

LangChain is a framework for building LLM-powered applications. This repository provides hands-on Python examples and tutorials for LangChain, demonstrating everything from basic use of language models to advanced agent workflows.  It includes examples of prompt templates, embeddings, chains, and agent usage.  Notably, it shows how to integrate LangChain with external services (for example, using OpenAI’s API for LLM/chat models) and vector databases (e.g. FAISS) for retrieval.  The code is organized as both Python scripts and a Jupyter notebook (`Model.ipynb`) so you can step through concepts interactively.

## Contents

* **1.LLMs/**: Examples of calling large language models (LLMs) such as OpenAI or HuggingFace models using LangChain’s LLM interfaces.
* **2.ChatModel/**: Demos of using chat-oriented models (e.g. `ChatOpenAI`) through LangChain’s chat model abstractions.
* **3.Embedding/**: Generating and using vector embeddings (e.g. `OpenAIEmbeddings`) and storing/searching them in a vector store like FAISS.
* **4.Prompts/**: Examples of crafting and using prompt templates and prompt engineering techniques in LangChain.
* **5.Output/**: Code showing how to handle and format the output from models (for instance, parsing responses or formatting results).
* **6.Chain\_Langchain/**: Building multi-step workflows (Chains) that link together LLM calls and tools into a pipeline.
* **8.AI\_agents/**: Examples of autonomous LangChain agents that can use tools or take actions (showcasing agent orchestration).
* **Model.ipynb**: A Jupyter notebook that ties together key concepts, with runnable examples for the above topics.
* **requirements.txt**: Lists the Python dependencies needed (LangChain, OpenAI, FAISS, etc.).
* **.gitignore**: Standard git ignore file to exclude unnecessary files from version control.

## Installation

1. Clone or download the repository to your local machine.
2. Ensure you have **Python 3.8+** installed.
3. (Optional) Create and activate a Python virtual environment.
4. Install required libraries with pip. For example:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the key packages manually. For instance:

   ```bash
   pip install langchain openai faiss-cpu PyPDF2 tiktoken
   ```

   (This matches a typical LangChain setup guide.)
5. Obtain any necessary API keys (e.g. an **OpenAI API key**) and set them in your environment. For example, set `OPENAI_API_KEY` before running the examples.

## Usage

* Open and run the `Model.ipynb` notebook in Jupyter to explore interactive examples of LangChain usage.
* To run specific demos, navigate into a folder (e.g. `1.LLMs/`) and run the Python scripts there. Each folder includes code for its topic.
* The code is organized to be explored in order: start with **1.LLMs**, then **2.ChatModel**, and progress through to **8.AI\_agents**. This way you build up from simple LLM calls to more complex chains and agents.
* Make sure your required environment variables (like `OPENAI_API_KEY`) are set before running scripts that call external models.

## Requirements

* **Python 3.8 or newer**.
* **LangChain** library (installable via `pip install langchain`).
* **OpenAI** Python package (for using OpenAI models).
* **FAISS** (e.g. the `faiss-cpu` package) for vector embeddings.
* **tiktoken** (for tokenization if needed).
* **PyPDF2** (used in PDF/document examples, as shown in some tutorials).
* Other packages listed in `requirements.txt`.

## License

This repository does not include a specific license file. All content is provided for educational purposes under the author’s permission. (Consult the repository owner for reuse details.)

**References:** LangChain documentation and examples.
