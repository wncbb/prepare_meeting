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
        self.deleted=False
    def getString(self):
        return ','.join([self.hostID, self.listingID, str(self.score), self.city])

def paginate(resultsPerPage, results):
    # Write your code here
    #print resultsPerPage
    #print results
    records=[]
    for row in results:
        curRst=row.split(",")
        r=Record(curRst[0], curRst[1], float(curRst[2]), curRst[3])
        records.append(r)
    records=sorted(records, key=lambda x: x.score, reverse=True)

    res=[]
    while True:
        curRes=getPage(records, resultsPerPage)
        print 'curRes', len(curRes)
        if len(curRes)!=0:
            res.append('#')
            res.extend(curRes)
        if len(curRes)<resultsPerPage:
            break
    
    return res



def getPage(records, pageSize):
    res=[]
    lookup=set()
    idx=0
    for r in records:
        if r.hostID in lookup:
            continue
        if r.deleted:
            continue
        lookup.add(r.hostID)
        res.append(r.getString())
        r.deleted=True
        idx=idx+1
        if idx==pageSize:
            return res
    if len(res)<pageSize:
        for r in records:
            if r.deleted:
                continue
            res.append(r.getString())
            idx=idx+1
            r.deleted=True
            if idx==pageSize:
                return res
    return res
    


        



    


resultsPerPage = 5
results = [
  "1,28,300.6,San Francisco",
  "4,5,209.1,San Francisco",
  "20,7,203.4,Oakland",
  "6,8,202.9,San Francisco",
  "6,10,199.8,San Francisco",

  "1,16,190.5,San Francisco",
  "6,29,185.3,San Francisco",
  "7,20,180.0,Oakland",
  "6,21,162.2,San Francisco",
  "2,18,161.7,San Jose",

  "2,30,149.8,San Jose",
  "3,76,146.7,San Francisco",
  "2,14,141.8,San Jose"]

rst=paginate(resultsPerPage, results)
print '----'
for v in rst:
    print v