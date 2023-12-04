from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = " This is our ML project with Modular coding"
AUTHOR_NAME = "Anvesh Reddy"
AUTHOR_EMAIL = "anveshbunty01@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

#Get Requirements.txt
#read
#/n ""
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("/n","") for requirement_name in requirement_list]
        
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
            
        return requirement_list

setup(name=PROJECT_NAME,
      version= VERSION,
      description=DESCRIPTION,
      author= AUTHOR_NAME,
      author_email= AUTHOR_EMAIL,
      packages=find_packages(),
      install_requries= get_requirements_list(),
      )