from setuptools import setup, find_packages

setup(
    name="sample_project",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    # Include non-Python files specified in MANIFEST.in
    include_package_data=True,
    install_requires=[
        "pytest>=7.0.0"
    ],
    python_requires=">=3.12",
)