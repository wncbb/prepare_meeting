# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Edge:
    def __init__(self, y, cost):
        self.y = y
        self.cost = cost
class Solution:
    """
    @param x: The vertex of edge
    @param y: The another vertex of edge
    @param cost: The cost of edge
    @param profit: The profit of vertex
    @return: Return the max score
    """
    def dfs(self, rt, father, G, profit):
        ans = 0
        assigned = False
        for line in G[rt]:
            if (line.y == father):
                continue
            if (assigned == True):
                ans = max(ans, self.dfs(line.y, rt, G, profit) - line.cost);
            else:
                ans = self.dfs(line.y, rt, G, profit) - line.cost
                assigned = True
        return ans + profit[rt]
    # x first node, y second node, cost of the edge, profit of the vertex
    def getMaxScore(self, x, y, cost, profit):
        
        G = [[] for i in range(len(profit))]
        for i in range(0, len(x)):
            line = Edge(y[i], cost[i])
            G[x[i]].append(line)
            line = Edge(x[i], cost[i])
            G[y[i]].append(line)
        return self.dfs(0, -1, G, profit)

x=[0,0]
y=[1,2]
cost=[1,2]
profit=[1,2,5]
s=Solution()
rst=s.getMaxScore(x, y, cost, profit)
print rst
