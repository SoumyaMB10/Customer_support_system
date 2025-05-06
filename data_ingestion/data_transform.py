import pandas as pd
from langchain_core.documents import Document

# transform/load the data
class data_converter:
    def __init__(self):
        print("data transformation initiated...")
        self.product_data = pd.read_csv(r"C:\Users\HP\Desktop\Customer_support_system\data\flipkart_product_review.csv")
        print(self.product_data.head())
        
    def data_transfomation(self):
        pass


if __name__ == "__main__":
    data_converter()