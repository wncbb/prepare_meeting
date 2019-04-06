# -*- encoding: utf8 -*-

from heapq import *

def buddyList(mlist, blists):
  cities = set([c for b in blists for c in b])
  print 'cities: ', cities
  idxs = {c: list() for c in cities}
  print 'idxs: ', idxs
  
  for i, blist in enumerate(blists):
    for c in blist:
      idxs[c].append(i)
  
  print 'idxs: ', idxs

  bcounts = [0]*len(blists)
  for mc in mlist:
    # 个人页面
    if mc in idxs:
      for b in idxs[mc]:
        bcounts[b]+=1
  print 'bcounts: ', bcounts
  return bcounts

def buddyListMax(mlist, blists):
  bcounts = buddyList(mlist, blists)
  return bcounts.index(max(bcounts))

def buddyListMaxK(mlist, blists, k):
  bcounts = buddyList(mlist, blists)
  minq = []
  for i,b in enumerate(bcounts):
    if len(minq)<k:
      heappush(minq, (b, i))
    elif minq[0][0]<b:
      heappop(minq)
      heappush(minq, (b, i))
  return minq

def buddyListRec(mlist, blists, k):
  """
  recommend k cities
  """
  bcounts = buddyList(mlist, blists)
  bcounts = [(c, i) for i, c in enumerate(bcounts)]
  bcounts.sort(key=lambda x: x[0], reverse=True)
  print bcounts
  rec = set()
  for cnt,i in bcounts:
    for city in blists[i]:
      if city not in mlist:
        rec.add(city)
        if len(rec)==k:
          return rec
  return rec

blists = [
["aa", "bb", "ee", "ff"],
["aa", "bb", "cc", "gg"],
["aa", "bb", "cc", "dd"],
["xx", "yy", "zz", "aa"]
  ]
mlist = ["aa", "bb", "cc", "dd"]

res=buddyListRec(mlist, blists, 3)
for v in res:
    print v
