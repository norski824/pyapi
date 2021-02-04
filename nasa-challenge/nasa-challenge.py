#!/usr/bin/python3

import requests


def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=gT8fYoCsl1LkiFELTUe1kBKSPpMgxAVoVGwSmG6F").json()
    nasa_data=[]
    for x in roverresp():
        print(x, ['rover'])
if __name__ == "__main__":
    main()
