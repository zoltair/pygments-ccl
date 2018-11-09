#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="CclLexer",
    version="0.1",
    packages=find_packages(),
    entry_points="""
[pygments.lexers]
ccl=ccl:CclLexer
""",
)
