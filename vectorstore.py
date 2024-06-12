from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from sentence_transformers import SentenceTransformer


def save_embed_model_to_local(model_name, model_path):
    """
    Save the embed model to local.
    """
    model = SentenceTransformer(model_name)
    model.save(model_path)


# 실험을 위해 허깅페이스 임베딩 사용 -> 향후 OpenAIEmbeddings로 교체
def load_embed_model_from_local(model_path):
    """
    Load the embed model from local.
    """
    embed_model = HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    return embed_model

def load_and_split_docs(doc_path):
    """
    Load and split the docs.
    """
    loader = PyMuPDFLoader(doc_path)
    docs = loader.load()

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=600,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    documents = text_splitter.split_documents(docs)

    return documents

def upload_to_vectorstore(documents, embed_model, persist_directory, collection_name):
    """
    Upload the docs to vectorstore.
    """
    vectorstore = Chroma.from_documents(
        documents, 
        embed_model,
        persist_directory=persist_directory,
        collection_name=collection_name,
        )
    return vectorstore

if __name__ == "__main__":
    model_name = "BAAI/bge-m3"
    model_path = "./models/bge-m3"

    save_embed_model_to_local(model_name, model_path)
    embed_model = load_embed_model_from_local(model_path)

    doc_path = "./data/2024 수능특강 화법과 작문.pdf"
    documents = load_and_split_docs(doc_path)

    upload_to_vectorstore(documents, embed_model, "./chroma_db", "speaking_and_writing")

