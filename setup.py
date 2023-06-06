from setuptools import setup, find_packages

long_description = None
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tiny-json",
    version="1.0",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Encode a JSON object to a small CSV string and decode that to the original JSON.",
    author="Greg  Silverman",
    author_email="silvermangb@gmail.com",
    install_requires=[],
    package_dir={"tiny-json": "src"},
)

