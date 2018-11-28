from setuptools import setup, find_packages

PACKAGES = find_packages(exclude=['tests', 'tests.*'])
VERSION = '0.1'

REQUIRES = [
    'requests',
    'pillow'
]

setup(
    name='machinebox-python-sdk',
    version=VERSION,
    url='https://github.com/machinebox/machinebox-python-sdk',
    keywords='machinebox',
    author='Robin Cole',
    author_email='robmarkcole@gmail.com',
    description='Tools for working with Machinebox',
    install_requires=REQUIRES,
    packages=PACKAGES,
    license='Apache License, Version 2.0',
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"]
)
