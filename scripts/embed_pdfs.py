import os
from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

PDF_FOLDER = "data/pdfs"
VECTORSTORE_PATH = "vectorstore/schemes_faiss_index.faiss"
METADATA_PATH = "vectorstore/metadata.pkl"

model = SentenceTransformer('all-MiniLM-L6-v2')
docs = []

for pdf_file in os.listdir(PDF_FOLDER):
    if pdf_file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(PDF_FOLDER, pdf_file))
        pdf_docs = loader.load()
        docs.extend(pdf_docs)

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)
texts = [chunk.page_content for chunk in chunks]
embeddings = model.encode(texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings, dtype=np.float32))

os.makedirs("vectorstore", exist_ok=True)
faiss.write_index(index, VECTORSTORE_PATH)

with open(METADATA_PATH, "wb") as f:
    pickle.dump(texts, f)

print(f"✅ Embedded {len(texts)} chunks and saved FAISS index.")
