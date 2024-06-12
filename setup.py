import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

setup(
    name='cda_download',
    version='0.0.4',
    packages=setuptools.find_packages(),
    url='http://github.com/paichiwo/cda_download',
    author='Lukasz Zerucha',
    author_email='lzerucha@gmail.com',
    description='A library that helps downloading videos from cda.pl',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    keywords=['cda', 'downloader', 'youtube-dl', 'pytube', 'video', 'cda_download']
)

install_requires = ['beautifulsoup4', 'selenium']
