from setuptools import find_packages, setup

setup(
    name= "e-commerce-bot",
    version = "0.0.1",
    author = "Soumya",
    email = "mbsoumya10@gmail.com",
    packages= find_packages(), # automaticaaly detects init files
    install_requires = ["langchain_astradb","langchain"]
)