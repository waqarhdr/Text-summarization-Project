# This is mostly required to publish it as pypy package and use it as plug and play 

import setuptools

with open('README.md', 'r', encoding="utf-8") as f:
    long_description = f.read() # This is required when you want to publish it in pypy package 

__version__ = "0.0.0"

REPO_NAME = "Text-summarization-Project"
AUTHOR_USER_NAME = "waqarhdr"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "waqarhdr134@gmail.com"  

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

