from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="shaq-freight",
    version="1.0.0",
    author="SHAQ Logistics",
    author_email="ayang@shaq-log.com",
    description="Free freight rate API client for global shipping routes from China",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://search.shaq-logistics.com",
    project_urls={
        "Documentation": "https://search.shaq-logistics.com/developers",
        "Freight Index": "https://search.shaq-logistics.com/freight-index",
        "Get Quote": "https://search.shaq-logistics.com/tools",
        "Bug Reports": "https://github.com/shaq-logistics/shaq-freight-python/issues",
        "Source": "https://github.com/shaq-logistics/shaq-freight-python",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.20.0",
    ],
    keywords="freight shipping logistics api ocean freight air cargo container shipping rate index fcl lcl china shipping",
)
