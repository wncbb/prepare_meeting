# -*- encoding: utf-8 -*-

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param heights: the height of the terrain
    @param V: the units of water
    @param K: the index
    @return: how much water is at each index
    """
    def outGraph(self):
        res=''
        maxLen=len(self.g[0])
        for i in range(1, len(self.g)):
            if len(self.g[i])>maxLen:
                maxLen=len(self.g[i])
        for i in range(0, len(self.g)):
            while len(self.g[i])<maxLen:
                self.g[i].append(' ')

        for i in range(maxLen-1, -1, -1):
            for j in range (len(self.g)):
                res=res+self.g[j][i]
            res+='\n'
        print res
        return res


    def printGraph(self):
        for v in self.g:
            print v
    def makeGraph(self, heights):
        g=[]
        for i, h in enumerate(heights):
            cur=[]
            for _ in range(h):
                cur.append('#')
            g.append(cur)
        self.g=g
    def graphAddWater(self, idx):
        self.g[idx].append('W')

    def pourWater(self, heights, V, K):
        self.makeGraph(heights)
        for _ in range(V):
            index=-1
            for i in range(K-1, -1, -1):
                if heights[i]>heights[i+1]:
                    break
                elif heights[i]<heights[i+1]:
                    index=i
            if index!=-1:
                heights[index]+=1
                self.graphAddWater(index)
                continue
            
            # should reasign index=-1
            index=-1
            for i in range (K+1, len(heights)):
                if heights[i]>heights[i-1]:
                    break
                elif heights[i]<heights[i-1]:
                    index=i
            if index!=-1:
                heights[index]+=1
                self.graphAddWater(index)
                continue
            
            heights[K]+=1
            self.graphAddWater(K)

        self.printGraph()
        return heights


heights = [2,1,1,2,1,2,2]
V = 4
K = 3
s=Solution()
rst=s.pourWater(heights, V, K)
s.printGraph()
s.outGraph()

# s=Solution()
# s.makeGraph(heights)
# s.printGraph()


