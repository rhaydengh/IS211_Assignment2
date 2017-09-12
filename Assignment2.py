#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 2, Part 1"""


import urllib2
import datetime
import logging
import arcparse
import csv

downloadData('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
processData(html)

def downloadData(url):
    """This function downloads data from a url"""
    str(url)
    response = urllib2.urlopen(url)
    global html
    html = response.read()
    return html.splitlines()

def processData(filetext):
    """This function processes contents from a data file, and returns a dictionary which maps 
    a person's ID to a tuple of the form (name, birthday),and logs incorrectly formatted dates to a logfile"""

    LOG_FILENAME = 'errors.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)
    logger = logging.getLogger('assignment2')

    newkey = parts[::2]
    global mydict
    mydict = {k: v for v, k in enumerate(newkey)}

    for key, val in mydict:
        try:
            mydict.keys() == datetime.datetime.strptime(row[2], '%d/%m/%Y')
        except ValueError:
            logger.error('Error processing line #' val '%s for ID # %s',
                         linenum, row[0])
            logfile = open(LOG_FILENAME, 'rt')
            try:
                output = logfile.read()
            finally:
                logfile.close()


def displayPerson(id, personData):
    """Displays a person's id and dob."""
    str(personID)
    int(id)

    try:
        print 'Person # {} is {} with a birthday of {}'.format(
        id, personData[personID][0], dict.keys())
    except:
        print 'No user found with that ID'

