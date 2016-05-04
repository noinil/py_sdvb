# py_sdvb

## Description

Vocabulary builder by generating word lists from stardict dictionaries.  Allow
**regular expression** search.  Written in python.


## Features

### Regular expression support

See some *regex* search examples below:

![Regex support.](/images/regex.png)

### Colored output

Keywords are highlighted.

<img src="/images/coloroutput.png"  width="800">



## Prerequisites

This package is based on `PyStarDict` (https://github.com/lig/pystardict).

Programs are tested for python3 on Mac OS X.


## Usage

### Get the dictionaries

Put all the dictionaries in the directory `~/.stardict/`.  If you have been
using tools like *stardict* or *sdcv*, you probably have already had the
dictionaries stored there.

### sdvb.py

This is the primary program to help building your vocabulary, by generating a
list of words together with their translations.

Run `sdvb.py` like this:
```bash
./sdvb.py [-s] [-h]
```

Use the `[-h]` option for help.

The `-s` option provides a mode to choose dictionary.  Otherwise, all the
dictionaries are used.

You will then be prompted with `REGEX:`, which askes you to input **regular
expressions** for search.


### sdcv.py

This is an interactive command line dictionary tool, basically an analog of
*sdcv*.

```bash
./sdcv.py
```

### Add to `$PATH`

```bash
ln -s /path/to/py_sdvb/sdvb.py /usr/local/bin/sdvb
ln -s /path/to/py_sdvb/sdcv.py /usr/local/bin/sdcv
```

