# -*- encoding: utf-8 -*-


# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

"""
Description
中文
English
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in lexicographical order
Have you met this question in a real interview?  
Example
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf"

Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".
"""

from heapq import heappush, heappop, heapify


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        graph = self.build_graph(words)
        print graph
        return self.topological_sort(graph)
        
    def build_graph(self, words):
        # key is node, value is neighbors
        graph = {}

        # initialize graph
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set() 

        # add edges        
        n = len(words)
        # 找前后两个单词之间相同位置的单词相对顺序，所以从0开始，到n-1
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    # TODO: really important
                    # the rest of odrders
                    break
                
        return graph

    def topological_sort(self, graph):
        # before looking into this part of code
        # you should know how to use bfs algorithm to do topological sorting
        # if you don't know, please google it first or join us at ä¹ç« ç®æ³ç­.
        
        # initialize indegree 
        indegree = {
            node: 0
            for node in graph
        }
        
        # calculate indegree
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] = indegree[neighbor] + 1

        # print indegree
        
        # use heapq instead of regular queue so that we can get the 
        # smallest lexicographical order
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)
        # print(queue)
        
        # regular bfs algorithm to do topological sorting
        topo_order = ""
        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)
            
        # if all nodes popped
        if len(topo_order) == len(graph):
            return topo_order
        
        return ""

s=Solution()

words=["ze","yf","xd","wd","vd","ua","tt","sz","rd", "qd","pz","op","nw","mt","ln","ko","jm","il", "ho","gk","fa","ed","dg","ct","bb","ba"]
s.alienOrder(words)
