import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
import os

# ===========================
# Securely get your OpenAI API key from environment variable
# ===========================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ===========================
# Streamlit User Interface
# ===========================

# App header
st.header("DocGPT: Chat with Your PDFs")

# Sidebar for file upload
with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader(
        "Upload a PDF file and start asking questions", 
        type="pdf"
    )

# ===========================
# Main logic: Executes if a file is uploaded
# ===========================
if file is not None:
    # 1. Extract text from the uploaded PDF file
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        # Extract text from each page (skip pages with no text)
        text += page.extract_text() or ""

    # 2. Split the extracted text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",      # Try to split on newline characters
        chunk_size=1000,      # Max chunk size in characters
        chunk_overlap=150,    # Overlapping characters between chunks
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # 3. Generate embeddings for each chunk using OpenAI embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # 4. Store embeddings in a FAISS vector store for similarity search
    vector_store = FAISS.from_texts(chunks, embeddings)

    # 5. Get user's question from the Streamlit input box
    user_question = st.text_input("Type your question here:")

    # 6. If a question is entered, find similar text chunks and generate an answer
    if user_question:
        # Find the most relevant chunks to the user's question
        match = vector_store.similarity_search(user_question)

        # Initialize the LLM (Large Language Model) for answering questions
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0,           # Set to 0 for deterministic output
            max_tokens=1000,         # Max answer length
            model_name="gpt-3.5-turbo"
        )

        # Load a QA (question-answering) chain
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(
            input_documents=match, 
            question=user_question
        )

        # Display the answer to the user
        st.write(response)