from setuptools import setup, find_packages

setup(
    name="leetcode-solutions",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest>=6.0",
        "pytest-cov>=2.0",
    ],
    extras_require={
        "dev": [
            "black",
            "mkdocs",
            "mkdocs-material",
            "mkdocstrings[python]",
        ]
    },
)
