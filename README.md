# py_sdvb

## Description

Vocabulary builder by generating word lists from stardict dictionaries.  Allow
regex search.  Written in python.


## Features

### Regular expression

### Colored output


## Usage

### Get the dictionaries

Put all the dictionaries in the directory `~/.stardict/`.  If you have been
using tools like *stardict* or *sdcv*, you probably have already had the
dictionaries stored there.

### sdvb.py

This is the primary program to help building your vocabulary, by generating a
list of words together with their translations.

Run this:
```bash
./sdvb.py
```
You will be prompted with `REGEX:`, which askes you to input **regular
expressions** for search.


### sdcv.py 

This is an interactive command line dictionary tool, basically an analog of
*sdcv*.

```bash
./sdcv.py
```

## Prerequisites

This package is based on the package `PyStarDict` (https://github.com/lig/pystardict).

Programs are tested for python3 on Mac OS X.
