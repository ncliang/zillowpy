from distutils.core import setup

setup(
    name = "zillowpy",
    packages = ["zillowpy"],
    version = "0.0.1",
    description = "A thin Python wrapper around the Zillow REST API",
    author = "Nigel Liang",
    author_email = "nigel@nigelliang.com",
    url = "https://github.com/ncliang/zillowpy",
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
)