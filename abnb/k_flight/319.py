# -*- encoding: utf-8 -*-
import collections

class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def add(self, a, b):
        if a==-1 or b==-1:
            return -1
        return a+b
    def getMin(self, a, b):
        if a==-1:
            return b
        if b==-1:
            return a
        return min(a, b)
    def findCheapestPrice(self, n, flights, src, dst, K):
        # write your code here
        lookup=collections.defaultdict()
        for i in range(n):
            lookup[i]=-1
        lookup[src]=0

        for i in range(K+1):
            curLookup=lookup.copy()
            for s, d, c in flights:
                curLookup[d]=self.getMin(curLookup[d], self.add(lookup[s], c))
            lookup=curLookup
        

        return lookup[dst]

"""
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
"""
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
s=Solution()
print s.findCheapestPrice(n, edges, src, dst, k)




