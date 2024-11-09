import os
os.environ['OPENAI_API_KEY'] = os.getenv('Key_OpenAI')
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import AzureOpenAIEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

import pathlib

#########################################################################
### env
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv('Key_OpenAI')
)

global sec_filling_db
global research_db
global news_db
global test

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


# adding html parser




# data_folder = "../../../Data"
#
# file_mapping = {
#     'sec_filling': f"{data_folder}/10k/",
#     'research_report': f'{data_folder}/research_reports/',
#     'news': f'{data_folder}/news/',
# }

def initialize_vector_store(file_mapping: dict):
    global sec_filling_db
    global research_db
    global news_db

    cwd = pathlib.Path.cwd()
    faiss_db_path = f"{cwd}/../../faiss-db/"


    if file_mapping:
        sec_filling_db = create_vector_database(file_mapping['sec_filling'])
        research_db = create_vector_database(file_mapping['research_report'])
        # news_db = create_vector_database(file_mapping['news'])

        # save the files
        sec_filling_db.save_local( faiss_db_path + "sec_filling_db")
        research_db.save_local( faiss_db_path + "research_report_db" )
        # news_db.save_local(faiss_db_path + "news_db")

    else:
        sec_filling_db = FAISS.load_local(faiss_db_path + "sec_filling_db", embeddings=embeddings, allow_dangerous_deserialization=True)
        research_db = FAISS.load_local(faiss_db_path + "research_report_db", embeddings=embeddings, allow_dangerous_deserialization=True)
        # news_db = FAISS.load_local(faiss_db_path + "news_db", embeddings=embeddings, allow_dangerous_deserialization=True)

# TODO: add the fuctionality of adding or deleting files from db
# thinking about add some process of selecting data files, summary then rag?


def global_test():
    global test
    test = 1


