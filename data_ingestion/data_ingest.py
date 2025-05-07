from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["ASTRA_DB_API_ENDPOINT"] = os.getenv("ASTRA_DB_API_ENDPOINT")
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
os.environ["ASRA_DB_KEYSPACE"] = os.getenv("ASRA_DB_KEYSPACE")

## push the data into VDB
class ingest_data:
    def __init__(self):
        print("data ingestion initiated....")
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        self.docs = data_converter.data_transfomation()

    def data_ingestion(self, status):
        vstore = AstraDBVectorStore(embedding=self.embeddings,
                           collection_name="chatbotecom",
                           api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
                           token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
                           namespace=os.environ["ASRA_DB_KEYSPACE"])
        storage = status
        if storage==None:
            inserted_ids = vstore.add_documents(self.docs)
            print(inserted_ids)
        else:
            return vstore
        
        return vstore, inserted_ids

## to check if the current file is corect and working 
if __name__ == '__main__':
    data_ingestion = ingest_data()
