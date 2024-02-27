from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filename:str)->List[str]:
    requirements=[]
    with open(filename) as file:
        requirements = file.readlines()
        
        requirements = [i.replace("","") for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name='DaimondPricePrediction',
    version='0.0.2',
    author='vikash',
    author_email='vikashrajverma89@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()




)