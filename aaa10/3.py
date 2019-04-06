#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'paginate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER resultsPerPage
#  2. STRING_ARRAY results
#
import collections

class Record:
    def __init__(self, hostID, listingID, score, city):
        self.hostID=hostID
        self.listingID=listingID
        self.score=score
        self.city=city
    def getString(self):
        return ','.join([self.hostID, self.listingID, str(self.score), self.city])

def paginate(resultsPerPage, results):
    