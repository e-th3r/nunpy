from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="nunpy",  
    version="0.1.0",   
    author="Maxim",
    author_email="maxim.perchikov@gmail.com",
    description="__",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/e-th3r/nunpy.git",  # Ссылка на репозиторий
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6", 
    install_requires=[],
)