"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages

setup(
    name='mihto',
    version='0.0.3',
    description='Easy and simple evaluation language',
    url='https://github.com/OrbitalAds/Mihto',
    author='OrbitalAds',
    author_email='dev@orbitalads.io',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='evaluation evaluate language',
    packages=find_packages(exclude=['docs', 'examples', 'tests'])
)
