from setuptools import setup, find_packages

setup(
    name='Class_07_OOP_Principles',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'termcolor',  # List other dependencies if any
    ],
    entry_points={
        'console_scripts': [
            'studysync=main:main',  # Replace 'main' with the function name you want to run
        ],
    },
)
