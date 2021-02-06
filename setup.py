from setuptools import setup, find_packages

__version__ = "0.2.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

TEST_REQUIREMENTS = [
    "pytest",
    "pytest-django",
    "pylint",
    "pylint_django",
]

setup(
    name="health-endpoint",
    version=__version__,
    author="ozacas",
    author_email="https://github.com/ozacas",
    description="A simple python/django DRF API endpoint using git repo data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ozacas/health-endpoint",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    tests_require=TEST_REQUIREMENTS,
    package_dir={"": "src"},
)
