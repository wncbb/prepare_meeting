# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Node:
    def __init__(self, idx, profit):
        self.idx=idx
        self.profit=profit
        self.children={}
    def addChild(self, nextIdx, cost):
        self.children[nextIdx]=cost

class Solution:
    def getMaxScore(self, x, y, cost, profit):
        nodes=[]
        for i in range(len(profit)):
            # print i
            # print profit
            nodes.append(Node(i, profit[i]))

        for i in range(len(x)):
            idx=x[i]
            node=nodes[idx]
            node.addChild(y[i], cost[i])
        self.result=0
        self.nodes=nodes
        self.dfs(self.nodes[0], 0)
        return self.result
        
    def dfs(self, root, curProfit):
        curProfit=curProfit+root.profit
        print 'curProfit:', curProfit
        if len(root.children)==0:
            if curProfit>self.result:
                self.result=curProfit
            return
        
        for nextIdx in root.children:
            curProfit-=root.children[nextIdx]
            print '39-curProfit:', curProfit, ' nextIdx:', nextIdx, ' nextCost:', root.children[nextIdx]
            self.dfs(self.nodes[nextIdx], curProfit)
            curProfit+=root.children[nextIdx]


x=[0,0]
y=[1,2]
cost=[1,2]
profit=[1,2,5]
s=Solution()
rst=s.getMaxScore(x, y, cost, profit)
print rst
