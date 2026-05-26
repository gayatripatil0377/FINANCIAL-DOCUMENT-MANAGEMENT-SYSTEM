from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from sentence_transformers import SentenceTransformer

import numpy as np
import faiss


model = SentenceTransformer("all-MiniLM-L6-v2")

db = faiss.IndexFlatL2(384)

pdf_data = []


def process_pdf(path):

    loader = PyPDFLoader(path)

    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(pages)

    text_data = []

    for doc in docs:

        text_data.append(doc.page_content)

    embeddings = model.encode(text_data)

    db.add(np.array(embeddings))

    pdf_data.extend(text_data)


def search_data(query):

    if len(pdf_data) == 0:

        return ["No Data Found"]

    embedding = model.encode([query])

    distance, index_number = db.search(
        np.array(embedding),
        5
    )

    result = []

    for i in index_number[0]:

        if i < len(pdf_data):

            result.append(pdf_data[i])

    return result