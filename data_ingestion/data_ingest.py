from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["ASTRA_DB_API_ENDPOINT"] = os.getenv("ASTRA_DB_API_ENDPOINT")
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
os.environ["ASRA_DB_KEYSPACE"] = os.getenv("ASRA_DB_KEYSPACE")

## push the data into VDB
class ingest_data:
    def __init__(self):
        print("data ingestion initiated....")
        pass

    def data_ingestion(self):
        pass

## to check if the current file is corect and working 
if __name__ == '__main__':
    data_ingestion = ingest_data()
