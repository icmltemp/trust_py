import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trust_py", 
    version="0.0.1",
    author="Trust ICML",
    author_email="",
    description="Code for Trust Function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/icmltemp/trust_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)