import chalk
import os, sys
from setuptools import setup, find_packages


def file_name(rel_path):
    dir_path = os.path.dirname(__file__)
    return os.path.join(dir_path, rel_path)

def read(rel_path):
    with open(file_name(rel_path)) as f:
        ret = f.read()
    return ret

def readlines(rel_path):
    with open(file_name(rel_path)) as f:
        ret = f.readlines()
    return ret

setup(
    author = "Anthony Almarza",
    author_email = "anthony@reeliolabs.com",
    name = "pychalk",
    packages = find_packages(),
    version = chalk.__version__,
    url = "https://github.com/anthonyalmarza/chalk",
    download_url = "https://github.com/anthonyalmarza/chalk/tarball/v"+chalk.__version__+"-beta",
    description = "Color printing in python",
    long_description = "Also includes a logging handler for printing in color.",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = ["print", "color", "chalk", "logging"],
)
