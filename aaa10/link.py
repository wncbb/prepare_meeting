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
        self.next=None
        self.prev=None
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
    firstRecord=Record('', '', 0, '')
    curRecord=firstRecord
    for i in range(0, len(records)):
        curRecord.next=records[i]
        records[i].prev=curRecord
        curRecord=curRecord.next

    res=[]
    while True:
        curRes=getPage(firstRecord, resultsPerPage)
        print 'cutRes: ', curRes
        print 'curRes', len(curRes)
        if len(curRes)!=0:
            res.extend(curRes)
            res.append('')
        if len(curRes)<resultsPerPage:
            break
        if curRecord is None:
            break
    
    return res



def getPage(r, pageSize):
    res=[]
    lookup=set()
    idx=0

    firstR=r

    while r is not None:
        if r.hostID=='':
            r=r.next
            continue
        if r.hostID in lookup:
            r=r.next
            continue
        lookup.add(r.hostID)
        res.append(r.getString())


        parent=r.prev
        child=r.next
        parent.next=child
        if child is not None:
            child.prev=parent

        r=child
        
        idx=idx+1
        if idx==pageSize:
            return res

    # for r in records:
    #     if r.hostID in lookup:
    #         continue
    #     if r.deleted:
    #         continue
    #     lookup.add(r.hostID)
    #     res.append(r.getString())
    #     r.deleted=True
    #     idx=idx+1
    #     if idx==pageSize:
    #         return res
    r=firstR
    if len(res)<pageSize:
        while r is not None:
            if r.hostID=='':
                r=r.next
                continue
            res.append(r.getString())

            parent=r.prev
            child=r.next
            parent.next=child
            if child is not None:
                child.prev=parent

            r=child

            idx=idx+1
            if idx==pageSize:
                return res
            
    return res
    

resultsPerPage = 1
results = [
'1,28,100.3,Paris',
'4,5,99.2,Paris',
'2,7,90.5,Paris',
'8,8,87.6,Paris'
 ]

rst=paginate(resultsPerPage, results)
for v in rst:
    print 'v:', v