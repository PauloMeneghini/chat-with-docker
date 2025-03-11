#pip install langchain-huggingface
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader

#%pip install -qU  langchain_milvus
from langchain_milvus import BM25BuiltInFunction, Milvus

from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

from create_milvus_db import createMilvusDB

def initialize_milvus():

    createMilvusDB()

    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

    #loader = PyPDFLoader('./data/dados.pdf')

    # Configurando o TextSplitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=300)

    documents = []

    # Listar todos os arquivos PDF na pasta './data'
    for file_name in os.listdir('./data'):
        if file_name.endswith('.pdf'):  # Verifica se o arquivo é um PDF
            file_path = os.path.join('./data', file_name)
            print(f"Carregando arquivo: {file_path}")
            
            # Carrega o conteúdo do PDF e divide em partes
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load_and_split(text_splitter=text_splitter))  # Adiciona as páginas à lista

            print(f"Arquivo carregado: {file_path}")

    print("Todos os arquivos foram carregados!")

    # for doc in documents:
    #     print(doc)
    
    URI = "http://localhost:19530"
    vector_store_saved = Milvus.from_documents(
        documents=documents, 
        embedding=embeddings, 
        connection_args={"uri": URI, "token": "root:Milvus", "db_name": "milvus_demo"},
        collection_name="LangChainCollection",
        index_params={"index_type": "FLAT", "metric_type": "L2"},
        consistency_level="Strong", 
        drop_old=True
    )

    vector_store_loaded = Milvus(
        embeddings,
        connection_args={"uri": URI},
        collection_name="LangChainCollection",
    )

    print(f"VECTOR saved: {vector_store_saved}")
    print(f"VECTOR LOADED: {vector_store_loaded}")

    return vector_store_saved