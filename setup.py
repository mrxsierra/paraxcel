from setuptools import setup, find_packages

setup(
    name="paraxcel",
    version="0.0.1",
    python_requires='>=3.12',
    packages=find_packages(where="src", exclude=["tests*"]),
    package_dir={"": "src"},
    
    # Include assets (icon.png in this case)
    package_data={
        "": ["assets/*.ico"],
    },
    
    install_requires=[
        "pandas",
        "python-docx",
        "pydantic",
        "openpyxl",
    ],
    entry_points={
        "console_scripts": [
            "paraxcel=src.app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
