# CHAT-PDF

PDF Reading and Question Answering using Language Models
This project explores the use of Language Models (LLMs) to extract information from PDF files and answer questions based on their content. The goal is to demonstrate the application of LLMs in natural language processing tasks involving document understanding.

### Before running the project:
 - insert your keys on .env file

    OPENAI_API_KEY=
    
    HUGGINGFACEHUB_API_TOKEN=

## Project Objective

The main objective of this project is to showcase an APP that shows how Language Models can be leveraged to read PDF documents, comprehend their content, and provide answers to questions posed by users.

## Features

- PDF parsing and text extraction using libraries like `PyMuPDF` (MuPDF) or other suitable tools.
- Utilization of pre-trained LLMs (e.g., BERT, GPT, HUGGINGFACE) for understanding the extracted text and answering questions.
- Interactive user interface (CLI, web interface, etc.) for users to input questions and receive answers.

## Project Structure

The project is structured as follows:

- **src/**: Source code for PDF parsing, text processor, chunck processor, conversation agent, LLM integration, and user interaction.
- **config/**: the configuration settings

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/CHAT-PDF.git
   ```

2. Install the dependences
   
```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
```
3. Run the project
```bash
  python src/app.py
 ```
