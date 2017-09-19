#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 2, Part 1"""


import urllib2
import datetime
import sys
import logging
import argparse
import csv
from StringIO import StringIO

def downloadData(url):
    """This function downloads data from a url"""

    data = urllib2.urlopen(url)
    html = data.read()


def processData(csvdata):
    """This function processes contents from a data file, and returns a dictionary which maps 
    a person's ID to a tuple of the form (name, birthday)"""

    LOG_FILENAME = 'errors.log'
    logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.ERROR,
                    )
    logger = logging.getLogger('assignment2')

    mydict = {}
    count_rows = 0
    reader = csv.reader(StringIO(html))
    for row in reader:
        try:
            """Returns row and numbers them"""
            count_rows += 1
            datetime.datetime.strptime(row[2], '%d/%m/%Y')
            mydict[row[0]] = (row[1], row[2])

        except ValueError:
            logger.error
            print("Error processing line #", count_rows, "for ID #", row[0])

    return mydict

def displayPerson(id, personData):
    id = raw_input("User ID: ")
    {int(key):personData[key] for key in personData}
    if id == personData[id]:
        print("Person #", id, "is", row[1], "with a birthday of", row[2])
    elif id != personData[id]:
        print 'no user found with that id'
    elif id in (0):
        raise SystemExit
    else: 
        ValueError:
            break
    
def main():
    csvData = downloadData(url)
    personData = processData(csvData)
    
if __name__ == "__main__":
    main()

