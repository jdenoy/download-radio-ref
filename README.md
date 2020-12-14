# download-radio-ref
Script to download the radio REF

## Installation
```
git clone https://github.com/jdenoy/download-radio-ref.git
cd download-radio-ref
pip install -r requirements.txt
```

## Configuration
Please edit sync.ini in same path, and change username and password.
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