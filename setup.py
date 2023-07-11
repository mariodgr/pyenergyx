from setuptools import setup, find_packages

setup(
    name='energyconverter', 
    version='0.1', 
    packages=find_packages(),
    description='A simple energy conversion library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mario David Gonzalez Ronda', 
    author_email='mariodgr@protonmail.com', 
    url='https://github.com/mariodgr/pyenergyx', 
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
