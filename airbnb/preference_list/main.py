import collections

class Solution:
    def buildGraph(self, lists):
        graph=collections.defaultdict(set)
        for l in lists:
            for i in range(1, len(l)):
                print 'sk', l[i-1], l[i]
                graph[l[i-1]].add(l[i])

        self.graph=graph

    def makeIndegrees(self):
        self.indegrees={}

        for src in self.graph:
            if src not in self.indegrees:
                self.indegrees[src]=0
            children=self.graph[src]
            for child in children:
                if child not in self.indegrees:
                    self.indegrees[child]=0
                self.indegrees[child]+=1

    def topoSort(self):
        print self.indegrees
        q=collections.deque()
        for item in self.indegrees:
            if self.indegrees[item]==0:
                q.append(item)

        res=[]
        while len(q)>0:
            item=q.popleft()
            res.append(item)
            for child in self.graph[item]:
                self.indegrees[child]-=1
                if self.indegrees[child]==0:
                    q.append(child)

        print 'res:', res
        return res

    def getList(self, lists):
        self.buildGraph(lists)
        self.makeIndegrees()
        self.topoSort()


s=Solution()
s.getList([
    [1, 2, 3],
    [1, 4, 5],
    [3, 4]
])


