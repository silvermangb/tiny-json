from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    setup(
        name="tiny-json",
        version="1.0",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        long_description=fh.read(),
        long_description_content_type="text/markdown",
        description="Encode a JSON object to a small CSV string and decode that to the original JSON.",
        author="Greg  Silverman",
        author_email="silvermangb@gmail.com",
        url="https://github.com/your_username/tiny-json",  # add your project's URL here
        classifiers=[
            'Development Status :: 3 - Alpha',  # or Beta, Stable
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        install_requires=[
            # list of dependencies
        ],
    )

