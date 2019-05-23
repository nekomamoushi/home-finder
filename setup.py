# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='home-finder',
    version='0.1',
    packages=find_packages(where='src', exclude=['contrib', 'docs', 'tests']),
    package_dir={"": "src"},
    author="author",
    author_email="email",
    description="A New Home",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='http://github.com/nekomamoushi/home-finder',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points = {
        'console_scripts': [
            'home-finder = home_finder.cli:cli',
        ],
    },
)
