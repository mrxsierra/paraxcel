from setuptools import setup, find_packages

setup(
    name="paraxcel",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-docx",  # Add other dependencies your project may have
        "pandas",
        "openpyxl",
        "pydantic",
        "pytest",
        "pytest-cov",
        # Add any other dependencies you need
    ],
    entry_points={
        "console_scripts": [
            "paraxcel=app:main",
        ],
    },
    package_data={
        '': ['*.txt', '*.md', '*.docx'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12.1',
)
