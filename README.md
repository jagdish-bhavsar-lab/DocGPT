# DocGPT: Chat with Your Documents

**DocGPT** is a lightweight chatbot built using [Streamlit](https://streamlit.io/), [LangChain](https://python.langchain.com/), [FAISS](https://github.com/facebookresearch/faiss), and [OpenAI GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5). It allows users to upload PDF documents and interact with them using natural language — getting answers straight from the document, not the internet.

---

## 🚀 Features

* Chat with any PDF (constitution, policy, textbook, etc.)
* LLM-powered answers — grounded in your uploaded data
* Clean, minimal Streamlit UI for interaction
* Vector search powered by FAISS
* All done with just 50 lines of Python code

---

## 🎯 Goal

Take user question ➔ convert to embedding ➔ semantic search on vector DB ➔ match relevant chunks ➔ send to LLM ➔ get final answer

---

## 🔁 Architecture Flow

```text
1. Upload files
2. Chunk documents
3. Generate embeddings
4. Store in FAISS vector DB
5. Accept user query
6. Convert query to embedding
7. Semantic search against vector DB
8. Retrieve matched chunks
9. Send chunks + question to LLM
10. Generate and return answer
```

---

## 🧰 Python Libraries Used

* [`streamlit`](https://streamlit.io/) → UI for user input/output
* [`PyPDF2`](https://pypi.org/project/PyPDF2/) → Extract text from PDFs
* [`langchain`](https://python.langchain.com/) → Chunking, embeddings, chain execution
* [`faiss-cpu`](https://github.com/facebookresearch/faiss) → Vector DB for similarity search

---

## 📦 Setup Instructions

**Prerequisites:** Python 3.8+

1. **Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/DocGPT.git
cd DocGPT
```

2. **Create and activate a virtual environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your OpenAI API Key**

* Create a `.env` file and add:

```
OPENAI_API_KEY=sk-...
```
*Or export it as an environment variable:*
```bash
export OPENAI_API_KEY=sk-...
```

5. **Run the app**

```bash
streamlit run app.py
```

---

## 📸 Screenshot

![App Screenshot](image1)

---

## 🛡 Security Tip

**Never expose your OpenAI API key in public repos.** Use `.env` and ensure it's gitignored.

---

## 📚 Bonus Insight

LangChain acts like the wiring here:

```
Chunks + Question ➔ Processed Chain ➔ LLM ➔ Answer
```

---

## 💡 Why This Matters

You can now create a chatbot that knows your internal docs, not just what GPT was trained on. Ideal for legal docs, SOPs, research papers, or customer manuals.

---

## 🧪 Example Use Cases

* Ask a PDF copy of the Indian Constitution, "Who can be President of India?"
* Upload your company policy and ask, "What’s the leave policy for probation employees?"

---

## ⚠ Disclaimer

This is a learning project. OpenAI API usage may incur costs. Optimize queries and avoid uploading large PDFs while experimenting.

---

## 🧑‍💻 Dev Note

Meanwhile, Java developers still need Spring Boot configs and annotations just to connect to a DB. 😅

---

## 🤝 Contributing

PRs welcome! Feel free to fork, improve, and share.

---

## 📄 License

MIT. Built for learning. Feel free to fork, extend, or experiment.