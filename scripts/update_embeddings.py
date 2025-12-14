import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


PDF_FOLDER = "data/pdfs"
VECTORSTORE_PATH = "vectorstore/schemes_faiss_index.faiss"
METADATA_PATH = "vectorstore/metadata.pkl"

model = SentenceTransformer('all-MiniLM-L6-v2')
existing_files = set()
if os.path.exists(METADATA_PATH):
    with open(METADATA_PATH, "rb") as f:
        existing_texts = pickle.load(f)
else:
    existing_texts = []

index = faiss.read_index(VECTORSTORE_PATH) if os.path.exists(VECTORSTORE_PATH) else None
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)

for pdf_file in os.listdir(PDF_FOLDER):
    if pdf_file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(PDF_FOLDER, pdf_file))
        pdf_docs = loader.load()
        chunks = splitter.split_documents(pdf_docs)
        texts = [chunk.page_content for chunk in chunks if chunk.page_content not in existing_texts]
        if not texts:
            continue
        embeddings = model.encode(texts)
        if index is None:
            index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(np.array(embeddings, dtype=np.float32))
        existing_texts.extend(texts)

os.makedirs("vectorstore", exist_ok=True)
faiss.write_index(index, VECTORSTORE_PATH)
with open(METADATA_PATH, "wb") as f:
    pickle.dump(existing_texts, f)

print("✅ FAISS index updated with new PDFs.")
