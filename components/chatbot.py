from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np
from groq import Groq
import os

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=api_key)


# Set Groq API Key
#os.environ["GROQ_API_KEY"] = "removedthekeyforprivacy"
#client = Groq(api_key=os.environ["GROQ_API_KEY"])

class GovernmentChatbot:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.read_index("vectorstore/schemes_faiss_index.faiss")
        with open("vectorstore/metadata.pkl", "rb") as f:
            self.text_chunks = pickle.load(f)

    def retrieve_context(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(query_embedding, dtype=np.float32),
            top_k
        )
        retrieved = [self.text_chunks[i] for i in indices[0]]
        return "\n\n".join(retrieved)

    def generate_answer(self, query):
        # Retrieve relevant context
        context = self.retrieve_context(query)

        prompt = f"""
You are an assistant helping rural citizens understand government schemes.

User Question:
{query}

Information from Government Documents:
{context}

Now generate the final answer in:
- Very simple rural-friendly language
- detail answer in easy language
- Bullet points and structured
- Clear points no mixing of points from other schemes
- show detailed answer based on the query
- An example for farmers / rural women
DO NOT mention that the answer is based on PDFs or context.
"""

        # Groq Llama-3 call
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {"role": "system", "content": "You simplify government schemes for rural India."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

