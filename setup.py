import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="transliterate-xon",
    version="0.0.1",
    author="Ismoilov Hamidullo",
    author_email="firstlike122@gmail.com",
    description="A transliteration library for easy transliteration of cyrillic or latin text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/firstlike122/transliterator",
    project_urls={
        "Bug Tracker": "https://github.com/firstlike122/transliterator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "transliterator"},
    packages=setuptools.find_packages(where="transliterator"),
    python_requires=">=3.6",
)