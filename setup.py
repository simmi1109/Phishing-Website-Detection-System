'''set up.py is used to install the package and its dependencies.
    it helps us use our project as a package and import it in other projects.
    example: pip install -e . (install the package in editable mode)
    from src.pipeline.predict_pipeline import PredictPipeline  )'''

from setuptools import find_packages, setup #this will help us find all the packages in our project and install them
    #whereve the __init__.py file is, this will allow to use it as a package
from typing import List # this is used to specify the type of the list of requirements

def get_requirements()-> List[str]: #what does this function do? it will return a list of requirements that are needed to install the package

    requirements_lst : List[str]= [] #this will be the list of requirements that we will return at the end of the function
    '''this function will read the requirements.txt file and return a list of requirements'''
    try:
        with open('requirements.txt', 'r') as f:
                #read the lines in the file
            lines=f.readlines()#this will return a list of lines in the file
                # process each line to remove any extra spaces and newlines
            for line in lines:
                requirements=line.strip() #this will remove any extra spaces and newlines
                # ignore empty spaces and e. (usually in the req.txt file
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements) #this will add the requirement to the list of requirements
    except Exception as e:
        print(f"requirements.txt file not found: {e}") #this will print an error message if the requirements.txt file is not found
            
    return requirements_lst #this will return the list of requirements

#print(get_requirements()) #this will print the list of requirements to the console

#creating metadata for the package
setup(
    name='network_security_project', #this is the name of the package
    version='0.0.1', #this is the version of the package
    author='Symniya Vindo Krishna', #this is the author of the package
    author_email= 'symniya09@gmail.com',
    description='A network security phishing detectionproject using machine learning and MLOps practices', #this is a short description of the package
    packages=find_packages(), #this will find all the packages in the project and include them in the installation
    install_requires=get_requirements() #this will install all the requirements that are needed to run the package
)