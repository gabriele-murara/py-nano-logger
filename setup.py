import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# We had to change the way requirements are loaded
# because they make problems with url requirements.
required_all = [i.strip() for i in open("requirements.txt").readlines()]


required = []

# add to required only the file entries which don't match
# with required_dev entries
for file_entry in required_all:
    required.append(file_entry)

setup(
    name='nano_logger',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple logger',
    install_requires=required,
    long_description=README,
    url='https://murara.computer/',
    author='Gabriele Murara',
    author_email='gabriele@murara.computer',
    classifiers=[
        'Environment :: command line',
        'Framework :: No',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
