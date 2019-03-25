from heapq import heappop, heappush, heapify
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def alienOrder(self, words):
        self.graph={}
        self.words=words
        self.result=''
        self.buildGraph()
        self.topoSort()

        if len(self.result)==len(self.graph):
            return self.result
        return ''


    def topoSort(self):
        indegrees=self.getIndegrees()
        print indegrees
        q=[]
        heapify(q)

        for k in indegrees:
            if indegrees[k]==0:
                heappush(q, k)

        while len(q)!=0:
            ch=heappop(q)
            self.result+=ch
            children=self.graph[ch]
            for child in children:
                indegrees[child]-=1
                if indegrees[child]==0:
                    heappush(q, child)


    def getIndegrees(self):
        indegreeLookup={}
        for word in words:
            for ch in word:
                indegreeLookup[ch]=0

        for k in self.graph:
            for v in self.graph[k]:
                indegreeLookup[v]+=1
        return indegreeLookup


    def buildGraph(self):
        for word in self.words:
            for ch in word:
                self.graph[ch]=set()

        for i in range(0, len(self.words)-1):
            word1=self.words[i]
            word2=self.words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j]!=word2[j]:
                    self.graph[word1[j]].add(word2[j])
                    break


s=Solution()

words=["ze","yf","xd","wd","vd","ua","tt","sz","rd", "qd","pz","op","nw","mt","ln","ko","jm","il", "ho","gk","fa","ed","dg","ct","bb","ba"]
print s.alienOrder(words)
