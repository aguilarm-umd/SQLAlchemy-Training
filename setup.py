from setuptools import find_packages, setup

setup(
    name='SQLAlchemy-Training',
    version='1.0.0',
    description='Test project for learning SQLAlchemy',
    author='Marc Andreu Grillo Aguilar',
    author_email="aguilarm@umd.edu",
    platforms=["any"],
    license="Apache",
    url="https://github.com/aguilarm-umd/SQLAlchemy-Training",
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    python_requires='>=3.7',
)
