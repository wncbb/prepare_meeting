class Solution:
    """
    @param bottom: a string
    @param allowed: a list of strings
    @return: return a boolean
    """
    def helper(self, level, nextLevel):
        if len(level)==2 and len(nextLevel)==1:
            self.result.append(nextLevel)
            return

        if (len(level)-1)==len(nextLevel):
            return self.helper(nextLevel, '')

        curLeft=level[len(nextLevel)]
        curRight=level[len(nextLevel)+1]
        curKey=curLeft+curRight
        if curKey not in self.lookup:
            return
        for v in self.lookup[curKey]:
            self.helper(level, nextLevel+v)


    def pyramidTransition(self, bottom, allowed):
        self.result=[]
        # write your code here
        lookup={}
        for v in allowed:
            if v[:2] not in lookup:
                lookup[v[:2]]=set()
            lookup[v[:2]].add(v[2])
        print lookup
        self.lookup=lookup
        self.helper(bottom, '')
        return self.result



s=Solution()
bottom="XYZ"
allowed=["XYD", "YZE", "DEA", "FFF", "XYM", "YZN", "MNB"]
print s.pyramidTransition(bottom, allowed)
