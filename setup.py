#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import the libraries
import setuptools

# Import the description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Initialize the setup
setuptools.setup(
    name = "delicate",
    version = "1.0.3",
    author = "Advent Group",
    author_email = "development@adventgroup.net",
    description = "Printing colored messages to the CLI",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/adventgroup/delicate",
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
)
