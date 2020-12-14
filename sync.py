#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from urllib3.exceptions import InsecureRequestWarning
import json
import sys
import configparser

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Parse configuration file to retrieve user/password for REF
config = configparser.ConfigParser()
config.sections()
config.read('sync.ini')
s_user = config['DEFAULT']['user']
s_pass = config['DEFAULT']['pass']


# Constant init
url = "https://espace.r-e-f.org//membres/radio-ref/telecharger.php"
referer = "https://espace.r-e-f.org//membres/radio-ref/dernier.php"


# Download function
def download(rcookie,year,month):
    
    r = requests.post(
        url,
        data = {'annee':year,'mois':month},
        auth=(s_user, s_pass), 
        verify=False,
        cookies=rcookie.cookies,
        headers={'referer': referer}
        )
    filename = "radioref-"+str(year)+"-"+str(month)+".pdf"
    print("Downloading radio REF of "+str(year)+"-"+str(month))
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

def main():

    #Variable init
    year = ""
    month = "" 
    if (len(sys.argv)>1):
        if sys.argv[1] in ('-h','--help'):
            print('Specify year, month as such : \n '+sys.argv[0]+' 2020 12')
            exit()
        if len(sys.argv) > 1:
            year = sys.argv[1]
        if len(sys.argv)>2:
            year = sys.argv[1]
            month = sys.argv[2]
            #Handle month givent a single number
            if len(month)==1:
                month="0"+str(month)
                print(month)
            #Handle july and august edition that are one and only edition
            if month in ('07','08'):
                month="07-08"
        if len(sys.argv)<1 or len(sys.argv)>3:
            print('Specify year, month as such : \n '+sys.argv[0]+' 2020 12')
            exit()

    rcookie = requests.get('https://espace.r-e-f.org//membres/radio-ref/dernier.php', auth=(s_user, s_pass), verify=False)

    if month=="":
        for month in ("01","02","03","04","05","06","07-08","09","10","11","12"):
            download(rcookie,year,month)
    else:
        download(rcookie,year,month)

# execute only if run as a script
if __name__ == "__main__":
    main()