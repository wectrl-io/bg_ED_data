#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

from setuptools import find_packages, setup

import bg_ED_data

#region File Attributes

__author__ = "Orlin Dimitrov"
"""Author of the file."""

__copyright__ = ""
"""Copyrighted"""

__credits__ = []
"""Credits"""

__license__ = ""
"""License
@see """

__version__ = "1.0.0"
"""Version of the file."""

__maintainer__ = ["Orlin Dimitrov", "Martin Maslyankov", "Nikola Atanasov"]
"""Name of the maintainer."""

__email__ = ""
"""E-mail of the author."""

#endregion

def long_description():
    """Long description reader.

    Returns:
        str: Long description text.
    """
    with open('README.md', encoding='utf-8') as file:
        return file.read()

install_requires = ["certifi==2022.12.7", "charset-normalizer==3.1.0",
                   "idna==3.4", "requests==2.28.2", "urllib3==1.26.15"],

setup(
    name="bg_ED_data",
    packages=find_packages(include=["bg_ED_data", 'bg_ED_data.*']),
    entry_points={
        'console_scripts': [
            'bg_ED_data = bg_ED_data.__main__:main'
        ]
    },
    version=__version__,
    description="Bulgaria electro distribution data provider.",
    long_description=long_description(),
    long_description_content_type='text/markdown',
    author=__author__,
    license=__license__,
    author_email=__email__,
    python_requires='>=3.7',
    install_requires=install_requires,
    setup_requires=[],
    tests_require=[],
    test_suite="",
    project_urls={
        'GitHub': 'https://github.com/wectrl-io/bg_ED_data',
    },
    classifiers=[
        'Development Status :: 1 - Debug',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Intended Audience :: Developers',
    ],
    # package_data={'example.path.lob.name': ['file_name.extension']}
)
