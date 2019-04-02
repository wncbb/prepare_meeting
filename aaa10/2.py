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
    # Write your code here
    print resultsPerPage
    print results
    records=[]
    for row in results:
        curRst=row.split(",")
        r=Record(curRst[0], curRst[1], float(curRst[2]), curRst[3])
        records.append(r)
    records=sorted(records, key=lambda x: x.score, reverse=True)

    idx=0
    lookup=set()
    res=[]
    dep=[]
    q=collections.deque()
    for r in records:
        q.push(r)
    while len(q)!=0:
        r=q.popleft()
        if r.hostID in lookup:
            q.push(r)
            continue
        res.append(r.getString())
        lookup.add(r.hostID)
        idx=idx+1
        if idx==resultsPerPage:
            idx=0
            lookup=set()
            res.append('#')
    if res[-1]=='#':
        res=res[:-1]
    return res
    




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    resultsPerPage = int(raw_input().strip())

    results_count = int(raw_input().strip())

    results = []

    for _ in xrange(results_count):
        results_item = raw_input()
        results.append(results_item)

    result = paginate(resultsPerPage, results)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
