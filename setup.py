from setuptools import setup
from setuptools import find_packages
from pathlib import Path

console_scripts = """
[console_scripts]
pod=lightning_pod.cli.main:main
"""

rootdir = Path(__file__).parent
long_description = (rootdir / "README.md").read_text()

requirements = [
    "click==8.1.3",
    "textual==0.1.18",
    "rich-cli==1.8.0",
    "colorama==0.4.5",
    "tabulate==0.8.10",
]

setup(
    name="lightning-pod",
    version="0.0.4.5",
    description="A Lightning.ai application seed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JustinGoheen/lightning-pod",
    author="Justin Goheen",
    author_email="",
    license="Apache 2.0",
    install_requires=requirements,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points=console_scripts,
    include_package_data=True,
)
