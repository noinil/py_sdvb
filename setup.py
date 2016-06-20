from setuptools import setup, find_packages

setup(
    name='py-sdvb',
    version='2.2',

    description='Dictionary interface of stardict, support regular expression (regex) search and colored output.',

    url='https://github.com/noinil/py_sdvb',
    download_url = 'https://github.com/noinil/py_sdvb/archive/v2.2.zip',

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
