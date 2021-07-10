from setuptools import find_packages, setup

setup(
    name='ColabTurtleClass',
    version='0.1.0',
    packages=find_packages(include=['ColabTurtleClass']),
    license='MIT',
    author='Kevin Shen',
    description='Class Implementation of ColabTurtle',
    url = 'https://github.com/abstrqt/ColabTurtleClass',
    install_requires=["IPython"]
)
