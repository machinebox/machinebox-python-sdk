from setuptools import setup

VERSION = '0.1'

setup(
    name='machinebox-sdk-python',
    version=VERSION,
    py_modules= ['facebox'],
    url='https://github.com/machinebox/sdk-python',
    keywords='facbox',
    author='who_is_this_to_be',
    author_email='get_official_email',
    description='Tools for working with Facebox',
    install_requires=['requests'],
    license='Apache License, Version 2.0',
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"]
)
