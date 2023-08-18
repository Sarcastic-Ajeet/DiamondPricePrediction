from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOTS="-e ."



def get_requiremens(file_paath:str)->List[str]:
    reqiurements=[]
    with open(file_paath) as file_obj:
        reqiurements=file_obj.readlines()
        reqiurements=[req.replace("\n","")for req in reqiurements]
        if HYPEN_E_DOTS in reqiurements:
            reqiurements.remove(HYPEN_E_DOTS)
        

    return reqiurements

    



setup(
    name="Diamond Price Prediction",
    version="0.0.1",
    author="sarcastic",
    author_email="example2gmail.com",
    packages=find_packages(),
    install_requirements=get_requiremens("requirements.txt")
)