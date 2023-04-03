#responsible to create the machine learning application as a package
from setuptools import find_packages,setup

setup(
name="ml_project",
version="0.0.1",
author="Hashir",
author_email="umairhashir89@gmail.com",
packages=find_packages(),
install_requires = ['pandas', 'seaborn', 'numpy']
)
