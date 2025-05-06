from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter

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
