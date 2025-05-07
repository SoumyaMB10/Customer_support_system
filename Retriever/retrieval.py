import os
from langchain_astradb import AstraDBVectorStore
from typing import List
from langchain_core.documents import Document
from config.config_loaders import load_config
from utils.model_loader import ModelLoader
from dotenv import load_dotenv
load_dotenv()


class Retriever:

    def __init__(self):
        self.model_loader = ModelLoader()
        self.load_config = load_config()
        self._load_env_variables()
        self.vstore = None
        self.retriever = None

    def _load_env_variables(self):
        required_vars = ["OPENAI_API_KEY", "ASTRA_DB_API_ENDPOINT", "ASTRA_DB_APPLICATION_TOKEN", "ASTRA_DB_KEYSPACE"]
        
        missing_vars = [var for var in required_vars if os.getenv(var) is None]
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.db_api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
        self.db_application_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
        self.db_keyspace = os.getenv("ASTRA_DB_KEYSPACE")

    def load_retriever(self):
        if not self.vstore:
            collection_name = self.load_config["astra_db"]["collection_name"]
            
            self.vstore = AstraDBVectorStore(
            embedding= self.model_loader.load_embeddings(),
            collection_name=collection_name,
            api_endpoint=self.db_api_endpoint,
            token=self.db_application_token,
            namespace=self.db_keyspace,
            )
        if not self.retriever:
            top_k = self.load_config["retriever"]["top_k"] if "retriever" in self.load_config else 3
            retriever = self.vstore.as_retriever(search_kwargs = {"k":top_k})
            print("retriever loaded successfully")
            return retriever

    def call_retriever(self, query:str)->List[Document]:
        retriever = self.load_retriever()
        output = retriever.get_relevant_documents(query)

        return output

if __name__ == '__main__':
    retriever_obj = Retriever()
    user_query = "can you suggest good budget laptop"
    results = retriever_obj.call_retriever(user_query)

    for idx, doc in enumerate(results,1):
        print(f"Results {idx}: {doc.page_content}\n Metadata: {doc.metadata}\n")
