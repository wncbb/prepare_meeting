
from heapq import *

def buddyListRec(myList, budyLists, num):
    budyLists=sorted(budyLists, key=lambda x: -len(set(x)&set(myList)))
    res=[]
    visited=set(myList)
    for budyList in budyLists:
        for city in budyList:
            if city not in visited:
                res.append(city)
                visited.add(city)
                if len(res)==num:
                    break
        if len(res)==num:
            break
    return res

blists = [
["aa", "bb", "ee", "ff"],
["aa", "bb", "cc", "gg"],
["aa", "bb", "cc", "dd"],
["xx", "yy", "zz", "aa"]
  ]
mlist = ["aa", "bb", "cc", "dd"]

res=buddyListRec(mlist, blists, 3)
print res