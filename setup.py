from setuptools import setup, find_packages

setup(
    name='py-sdvb',
    version='1.6.3',

    description='Dictionary interface of stardict, support regular expression (regex) search and colored output.',

    url='https://github.com/noinil/py_sdvb',

    author='Cheng Tan',
    author_email='noinil@gmail.com',

    license='GPL3',

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='dictionary, stardict, vocabulary builder, English, Chinese',

    packages = ['py-sdvb'],

    install_requires=['pystardict'],

    entry_points={
        'console_scripts': [
            'pysdcv=py-sdvb.sdcv:translate_word',
            'pysdvb=py-sdvb.sdvb:select_dictionary',
        ],
    },
)
