# Random Number List Generator

## Solution for Scenario 1

### Overview

The script will generate numbers from 1 to 10,unless a range specfied by the user on the terminal.

## Requirments

#### Python 3.8+


### Installation
#### Mac
- [Refer for MacOS](https://docs.python-guide.org/starting/install3/osx/)
    ```
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    export PATH="/usr/local/opt/python/libexec/bin:$PATH"
    brew install python
   ```
#### Linux
- [Refer for Linux](https://docs.python-guide.org/starting/install3/linux/)
    ```
        $ sudo apt-get update
        $ sudo apt-get install python3.6
    ```
### Packages
``` 
pip3 install argparse
pip3 install random
```

## Steps to run

- Clone this repo
- Execute the script `randomNumListGenerator.py`
    - script takes range as an argument `-r`
    - if no value is passed for `-r` then by default `10` is set to range
    - range argument `-r` takes only `int` type  

    ```
        python3 randomNumListGenerator.py -h
        usage: randomNumListGenerator.py [-h] [-r RANGE]
    
        Random number generator
    
        optional arguments:
            -h, --help            show this help message and exit
            -r RANGE, --Range RANGE
                             Specify range for generating a list, Default value is set 10 if no value is passed
    ``` 
- ## Example
    ```
    python3 randomNumListGenerator.py
    3 9 8 10 6 1 4 5 2 7
    ```
    ```
    python3 randomNumListGenerator.py -r 12
    2 4 10 5 6 8 12 3 7 1 9 11
    ```