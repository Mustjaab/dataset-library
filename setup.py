# setup.py
from setuptools import setup, find_packages

setup(
    name="marimo_data_loader",
    version="0.1",
    packages=find_packages(),
    description="A module that loads premade, editable datasets using marimo.",
    author="Muhammad Mustjaab",
    author_email="mustjaab.19@gmail.com",
    license="MIT",
    install_requires=[
        "pandas",
        "marimo"],  # Add any dependencies here if needed
)
