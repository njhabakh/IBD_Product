import pandas as pd
from langchain_community.vectorstores import FAISS

##################################################
# yahoo finance

def stock_prices(ticker: str) -> pd.DataFrame:
    """
    Get the historical prices and volume for a ticker for the last month.

    Args:
    ticker (str): the stock ticker to be given to yfinance

    """

    return pd.DataFrame(1)


def stock_news(ticker: str) -> list:
    """
    Get the most recent news of a stock or an instrument from Yahoo Finance

    Args:
    ticker (str): the stock ticker to be given to yfinance
    """

    return []


def db_retrieve(db: FAISS, query: str) -> str:
    """
    Retrieve the relevant information and print out
    """
    retriever = db.as_retriever()
    resources = retriever.get_relevant_documents(query)

    text_result = ""
    for resource in resources:
        metadata = resource.metadata
        content = resource.page_content
        text = f"From document {metadata['source']} page {metadata['page']}, we have following information. \n {content} \n"
        text_result = text_result + text

    return text_result


# news retrieve
def news_retrieve(query: str) -> str:
    global news_db
    return db_retrieve(news_db, query)

def research_retrieve(query: str) -> str:
    global research_db
    return db_retrieve(research_db, query)

def sec_filling_retrieve(query: str) -> str:
    global sec_filling_db
    return db_retrieve(sec_filling_db, query)


