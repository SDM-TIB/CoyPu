#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=7', ]

setup(
    author="Akhilesh Vyas",
    author_email='akh.vyas@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: Unknown',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="A Coypu python project ",
    entry_points={
        'console_scripts': [
            'coypu=coypu.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['coypu','coypu_project', 'l3s', 'vyas'],
    name='coypu_project',
    packages=find_packages(include=['coypu', 'coypu.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SDM-TIB/CoyPu',
    version='0.1.0',
    zip_safe=False,
)