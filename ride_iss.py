#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachement (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    # show that at this point, our data is str
    # we want to convert this to list / dict
    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))

    # this should say bytes
    print(type(helmet))

    # this should say dict
    print(type(helmetson))

    print(helmetson["number"])

    # this returns a LIST of the people on this ISS
    print(helmetson["people"])

    # list the FIRST astro in the list
    print(helmetson["people"][0])

    # list the SECOND astro in the list
    print(helmetson["people"][1])

    # list the LAST astro in the list
    print(helmetson["people"][-1])

    print("People in space: " + str(helmetson["number"]))


    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        
        print(astro["name"] + " is on the " + astro["craft"])

    ##display every item in a list
   
if __name__ == "__main__":
    main()

