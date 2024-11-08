import os
os.environ['OPENAI_API_KEY'] = os.getenv('Key_OpenAI')
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import AzureOpenAIEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

#########################################################################
### env
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv('Key_OpenAI')
)


def create_vector_database(file_path: str):
    loader=PyPDFDirectoryLoader(file_path)
    docs=loader.load()

    documents = RecursiveCharacterTextSplitter(
        chunk_size=1000, separators=["\n","\n\n"], chunk_overlap=200
    ).split_documents(docs)

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    return vector_store



data_folder = "../../../Data"

file_mapping = {
    'sec_filling': f"{data_folder}/10k/",
    'research_report': f'{data_folder}/research_reports/',
    'news': f'{data_folder}/news/',
}

def initialize_vector_store(fill_mapping: dict):
    global sec_filling_db
    global research_db
    global news_db

    sec_filling_db = create_vector_database(file_mapping['sec_filling'])
    research_db = create_vector_database(file_mapping['research_report'])
    news_db = create_vector_database(file_mapping['news'])



