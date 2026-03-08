from setuptools import find_packages,setup   # setuptools se functions import kiye packaging aur packages detect karne ke liye
from typing import List                      # type hint ke liye, batata hai function list return karega

HYPEN_E_DOT = '-e .'                         # requirements.txt me editable install ka symbol (current project ko install karta hai)

def get_requirements(file_path:str)->List[str]:   # function jo requirements.txt ka path lega aur dependencies list return karega
    '''
    This function will return the list of requirements
    '''
    requirements=[]                           # dependencies store karne ke liye empty list

    with open(file_path) as file_obj:         # requirements.txt file open karna
        requirements = file_obj.readlines()   # file ki saari lines (libraries) read karna

        requirements = [req.replace("\n","") for req in requirements]   # newline remove karna taaki clean library names mile

        if HYPEN_E_DOT in requirements:       # check karna ki '-e .' list me hai ya nahi
            requirements.remove(HYPEN_E_DOT)  # remove karte hain kyunki ye current project ko install karta hai, dependency nahi hai

    return requirements                       # final clean dependencies list return

setup(
    name='mlproject',                        # project/package ka naam
    version = '0.0.1',                       # project version
    author='Subhasish',                      # author ka naam
    author_email='subhasishs111@gmaill.com', # author email
    packages=find_packages(),                # automatically saare folders find karega jisme __init__.py hai
    install_requires = get_requirements('requirements.txt')  # requirements.txt se dependencies install karega
)