import yaml

def load_config(config_path:str = r"C:\Users\HP\Desktop\Customer_support_system\config\config.yaml")-> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config