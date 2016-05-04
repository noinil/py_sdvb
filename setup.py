from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-sdvb',
    version='1.6',

    description='Dictionary interface of stardict, support regular expression (regex) search and colored output.',
    long_description=long_description,

    url='https://github.com/noinil/py_sdvb',

    author='Cheng Tan',
    author_email='noinil@gmail.com',

    license='GPL3',

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='dictionary, stardict, vocabulary builder, English, Chinese',

    packages = ['pysdvb'],

    install_requires=['pystardict'],

    entry_points={
        'console_scripts': [
            'pysdcv=pysdvb.sdcv:translate_word',
            'pysdvb=pysdvb.sdvb:select_dictionary',
        ],
    },
)
