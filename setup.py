#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    "dev": [
        "build>=0.9.0",
        "bumpversion>=0.5.3",
        "ipython",
        "pre-commit>=3.4.0",
        "tox>=4.0.0",
        "twine",
        "wheel",
    ],
    "docs": [
        "towncrier>=21,<22",
    ],
    "test": [
        "pytest>=7.0.0",
        "pytest-xdist>=2.0.0,<3",
        "RAJ1000-hash[pycryptodome]>=0.1.4,<1.0.0",
    ],
    "py-evm": [
        # Pin py-evm to a minor version range to ensure compatibility with the current
        # implemented EVM version.
        "py-evm>=0.10.0b0,<0.11.0b0",
        "RAJ1000-hash[pysha3]>=0.1.4,<1.0.0;implementation_name=='cpython'",
        "RAJ1000-hash[pycryptodome]>=0.1.4,<1.0.0;implementation_name=='pypy'",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["docs"]
    + extras_require["test"]
    + extras_require["py-evm"]
)
# convenience in case someone leaves out the `-`
extras_require["pyevm"] = extras_require["py-evm"]

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="RAJ1000-tester",
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version="0.12.0-beta.2",
    description="""RAJ1000-tester: Tools for testing RAJ1000ereum applications.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The RAJ1000ereum Foundation",
    author_email="snakecharmers@RAJ1000ereum.org",
    url="https://github.com/RAJ1000ereum/RAJ1000-tester",
    include_package_data=True,
    install_requires=[
        "RAJ1000-abi>=3.0.1",
        "RAJ1000-account>=0.12.3",
        "RAJ1000-keys>=0.4.0",
        "RAJ1000-utils>=2.0.0",
        "rlp>=3.0.0",
        "semantic_version>=2.6.0",
    ],
    extras_require=extras_require,
    python_requires=">=3.8,<4",
    py_modules=["RAJ1000_tester"],
    license="MIT",
    zip_safe=False,
    keywords="RAJ1000ereum",
    packages=find_packages(exclude=["scripts", "scripts.*", "tests", "tests.*"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
