
import os
import streamlit as st
import requests
try:
    for key in ("VOYAGE_API_KEY", "GROQ_API_KEY"):
        if key in st.secrets:
            os.environ[key] = st.secrets[key]
except Exception:
    pass

from backend.knowledge_base import index_pdf
from backend.semantic_search import search_chunks
from backend.answer_generator import generate_answer

st.set_page_config(
    page_title="Nexus AI",
    page_icon="✦",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b1020;
        color: #f1f5f9;
    }
    .stTextArea textarea {
    color: #f1f5f9 !important;
    background-color: #151f38 !important;
    caret-color: #f1f5f9 !important;
    }

    .stTextArea textarea::placeholder {
        color: #aab7cf !important;
        opacity: 1 !important;
    }
    .block-container {
        max-width: 1050px;
        padding-top: 3rem;
    }

    .hero {
        padding: 2rem;
        border: 1px solid #293653;
        border-radius: 18px;
        background: linear-gradient(135deg, #151f38, #101729);
        margin-bottom: 1.5rem;
    }

    .subtitle {
        color: #aab7cf;
        font-size: 1.05rem;
    }

    div.stButton > button {
        border-radius: 10px;
        min-height: 2.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>✦ Nexus AI</h1>
        <p class="subtitle">
            Enterprise Knowledge Assistant
        </p>
        <p>
            Your workspace for exploring knowledge
            across enterprise documents.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


st.divider()

st.subheader("Upload your knowledge document")
st.caption("Upload a PDF to prepare it for semantic search.")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
    key="knowledge_pdf",
)

if uploaded_file is not None:
    if st.button("Process document", type="primary"):
        with st.spinner(
            "Extracting text and creating embeddings..."
        ):
            try:
                indexed_chunks = index_pdf(
                    uploaded_file.getvalue(),
                    chunk_size=180,
                    overlap=30,
                )

                if indexed_chunks:
                    st.session_state["indexed_chunks"] = (
                        indexed_chunks
                    )
                    st.session_state["document_name"] = (
                        uploaded_file.name
                    )

                    st.success(
                        f"Successfully indexed "
                        f"{len(indexed_chunks)} chunks."
                    )
                else:
                    st.warning(
                        "No readable text was found in this PDF."
                    )

            except Exception:
                st.error(
                    "Could not process the document. "
                    "Check the PDF and API configuration, "
                    "then try again."
                )

if "document_name" in st.session_state:
    st.caption(
        f"Current document: "
        f"{st.session_state['document_name']}"
    )

st.divider()

st.subheader("Ask your knowledge base")

st.caption(
    "Ask questions about your indexed documents."
)

question = st.text_area(
    "Your question",
    placeholder="Example: What are the main company policies?",
    height=120,
)


if st.button("Ask Nexus AI", type="primary"):
    if not question.strip():
        st.warning("Please enter a question first.")

    elif "indexed_chunks" not in st.session_state:
        st.warning("Please upload and process a PDF first.")

    else:
        try:
            with st.spinner("Searching your document..."):
                results = search_chunks(
                    query=question,
                    indexed_chunks=st.session_state["indexed_chunks"],
                    top_k=3,
                )

            if not results:
                st.info("No relevant passages were found.")

            else:
                with st.spinner("Generating an AI answer..."):
                    answer = generate_answer(
                        question=question,
                        retrieved_chunks=results,
                    )

                st.subheader("Answer")
                st.markdown(answer)

                st.subheader("Retrieved sources")

                for i, result in enumerate(results, start=1):
                    with st.expander(f"Source {i}"):
                        st.write(result["text"])
                        st.caption(
                            f"Similarity score: {result['score']:.3f}"
                        )

        except Exception:
            st.error(
                "Something went wrong while processing your question. "
                "Check the API configuration and terminal for details."
            )


st.caption("Nexus AI · Prototype v0.1")
