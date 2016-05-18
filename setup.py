from setuptools import setup, find_packages


version = '1.1.0'


setup(
    author="Anthony Almarza",
    author_email="anthony@reeliolabs.com",
    name="pychalk",
    packages=find_packages(),
    version=version,
    url="https://github.com/anthonyalmarza/chalk",
    download_url="https://github.com/anthonyalmarza/chalk/tarball/" + version,
    description="Color printing in python",
    long_description="Also includes a logging handler for printing in color.",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=['six', ],
    extras_require={'dev': ['ipdb', 'tox', 'coverage']},
    keywords=["print", "color", "chalk", "logging"],
)
