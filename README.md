# download-radio-ref
Script to download the Radio REF.
You need a proper subscription with the REF to be able to download the Radio REF magazine.

## Installation
```
git clone https://github.com/jdenoy/download-radio-ref.git
cd download-radio-ref
pip install -r requirements.txt
```

## Configuration
Please edit sync.ini in same path, and change REF username and password.
```
[DEFAULT]
user = callsign
pass = password
```

## Usage
```
$ python sync.py --help
usage:
  sync.py 2020 01           Download Radio REF for January 2020
  sync.py 2020              Download Radio REF for all months of 2020
```

## Requirements
* pip
* Python 3
* configparser (lib)
* requests (lib)