import streamlit as st
import os
import dotenv
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Load environment variables
dotenv.load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Ensure event loop exists for Gemini
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Streamlit setup
st.set_page_config(page_title="📘 Talk with PDF", layout="wide")
st.title("📘 Talk with PDF")

pdf_file = st.file_uploader("Upload a textbook or PDF notes", type="pdf")

if pdf_file:
    st.success("✅ PDF uploaded successfully!")

    # Save the file
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())

    # Load PDF
    with st.spinner("📖 Reading and analyzing the PDF..."):
        loader = PyPDFLoader("temp.pdf")
        pages = loader.load()
        full_text = "\n".join([p.page_content for p in pages])

        # Split for embeddings
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(pages)

        # Vector store (with persistent cache)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectordb = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="./chroma_db")
        retriever = vectordb.as_retriever()
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # User Q&A
    query = st.text_input("🔍 Ask a question about the document:")
    if query:
        with st.spinner("🤖 Generating response..."):
            answer = qa_chain.run(query)
            st.markdown("### 📌 Answer")
            st.write(answer)

    # Summary and Notes Options
    with st.expander("📄 Generate Summary & Notes"):
        col1, col2 = st.columns([1, 1])

        unit_notes = col1.button("🧠 Unit/Chapter-wise Summary & Notes")
        fallback_notes = col2.button("📘 General Important Notes")

        if unit_notes:
            with st.spinner("🧠 Detecting structure and summarizing..."):
                prompt = f"""
You're an expert tutor. Carefully read the following academic document.

If the document contains units or chapters, extract:
- Unit or Chapter Titles
- A 2–3 line summary per unit/chapter
- Key points in bullet format under each section.

If units or chapters are not found, provide:
- A general overview
- Categorized key concepts, definitions, and important notes.

Ensure formatting is clean and useful for students.

Text:
{full_text}
"""
                result = llm.invoke(prompt)
                st.markdown("### 📘 Unit/Chapter-wise Summary or Structured Notes")
                st.write(result.content)

        if fallback_notes:
            with st.spinner("🧠 Extracting important notes..."):
                prompt = f"""
You're a note-making assistant for students. From the following document, create:

- Key definitions
- Core concepts
- Important formulas or diagrams (describe if any)
- Use headings and bullet points

Make it organized and easy to revise.

Text:
{full_text}
"""
                result = llm.invoke(prompt)
                st.markdown("### 📋 Important Notes")
                st.write(result.content)
