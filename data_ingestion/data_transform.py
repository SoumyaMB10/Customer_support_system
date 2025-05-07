import pandas as pd
from langchain_core.documents import Document

# transform/load the data
class data_converter:
    def __init__(self):
        #print("data transformation initiated...")
        self.product_data = pd.read_csv(r"C:\Users\HP\Desktop\Customer_support_system\data\flipkart_product_review.csv")
        #print(self.product_data.head())
        
    def data_transfomation(self):
        required_col = self.product_data.columns[1:]
        #print(required_col)
        product_list = []
        for index, row in self.product_data.iterrows():
            object = {
                "product_name" : row["product_title"],
                "product_rating" : row["rating"],
                "product_summary" : row["summary"],
                "product_review" : row["review"],
            }
            product_list.append(object)
        #print(product_list)
        docs = []
        for entry in product_list:
            metadata = {"product_name":entry["product_name"],
                        "product_rating":entry["product_rating"],
                        "product_summary":entry["product_summary"]}
            doc = Document(page_content=entry["product_review"], metadata = metadata)
            docs.append(doc)

        return docs






if __name__ == "__main__":
    data_transform = data_converter().data_transfomation()