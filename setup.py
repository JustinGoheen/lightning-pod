import os
from setuptools import setup
from setuptools import find_packages
from pathlib import Path

rootdir = Path(__file__).parent
long_description = (rootdir / "README.md").read_text()

setup(
    name="lightning-pod",
    version="0.0.1",
    description="a Lightning.ai application seed",
    long_description=long_description,
    url="https://github.com/JustinGoheen/lightning-pod",
    author="Justin Goheen",
    license="Apache 2.0",
    install_requires=[],
    author_email="",
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)
