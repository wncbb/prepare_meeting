# -*- encoding: utf-8 -*-

from heapq import heappush, heappop, heapify

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def alienOrder(self, words):
        # write your code here
        # TODO: check params
        graph=self.buildGraph(words)
        print graph

        #  print graph

        inDegree=self.buildInDegree(words, graph)

        # print inDegree

        q=[]
        for i in inDegree:
            if inDegree[i]==0:
                q.append(i)
        heapify(q)

        ret=""
        while len(q)!=0:
            print q
            curChar=heappop(q)
            ret=ret+curChar
            for nextChar in graph[curChar]:
                inDegree[nextChar]-=1
                if inDegree[nextChar]==0:
                    heappush(q, nextChar)

        if len(ret)==len(graph):
            return ret  
        return ""
        
    def buildInDegree(self, words, graph):
        inDegree={}
        # 必须遍历words里的每一个单词每一个字母
        # 否则，有些不会在graph中出现
        # 在入度为0的检查时就会漏掉
        for word in words:
            for ch in word:
                inDegree[ch]=0
    
        for i in graph:
            for nextChar in graph[i]:
                if nextChar not in inDegree:
                    inDegree[nextChar]=0
                inDegree[nextChar]+=1
        return inDegree
        
    def buildGraph(self, words):
        graph={}
        # 必须遍历words里的每一个单词每一个字母
        # 否则，有些不会在graph中出现
        # 在入度为0的检查时就会漏掉
        for word in words:
            for ch in word:
                graph[ch]=set()

        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j]!=words[i+1][j]:
                    if words[i][j] not in graph:
                        graph[words[i][j]]=set()
                    graph[words[i][j]].add(words[i+1][j])
                    # 非常重要
                    # 这个字母不一样，后面的顺序是没有意义的
                    break
        return graph


s=Solution()

words=["ze","yf","xd","wd","vd","ua","tt","sz","rd", "qd","pz","op","nw","mt","ln","ko","jm","il", "ho","gk","fa","ed","dg","ct","bb","ba"]
print s.alienOrder(words)

"""
time: 建图->O(n*k), Topological sort-> O(26 + n) = O(n)
space: O(n)，主要是Map的大小
k表示单词平均长度
"""
