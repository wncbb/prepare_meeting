# -*- coding: utf-8 -*-
"""
Description
中文
English
Given a board which is a 2D matrix includes a-z and dictionary dict, find the largest collection of words on the board, the words can not overlap in the same position. return the size of largest collection.

The words in the dictionary are not repeated.
You can reuse the words in the dictionary.
Have you met this question in a real interview?
Example
Give a board below

[['a', 'b', 'c'],
 ['d', 'e', 'f'],
 ['g', 'h', 'i']]
dict = ["abc", "cfi", "beh", "defi", "gh"]
Return 3 // we can get the largest collection["abc", "defi", "gh"]

Related Problems
"""

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class TrieNode(object):
    def __init__(self, value=0):
        self.value = value
        self.isWord = False
        self.children = collections.OrderedDict()
        
    @classmethod
    def insert(cls, root, word):
        p = root
        for c in word:
            child = p.children.get(c)
            if not child:
                child = TrieNode(c)
                p.children[c] = child
            p = child

        p.isWord = True


class Solution:
    # @param {char[][]} board a list of lists of char
    # @param {str[]} words a list of string
    # @return {int} an integer
    def boggleGame(self, board, words):
        # Write your code here
        self.board = board
        self.words = words
        self.m = len(board)
        self.n = len(board[0])
        self.results = []
        self.temp = []
        self.visited = [[False for _ in xrange(self.n)] for _ in xrange(self.m)]
        
        self.root = TrieNode()
        for word in words:
            TrieNode.insert(self.root, word)
        
        self.dfs(0, 0, self.root)
                
        return len(self.results)
        
    def dfs(self, x, y, root):
        for i in xrange(x, self.m):
            for j in xrange(y, self.n):
                paths = []
                temp = []
                self.getAllPaths(i, j, paths, temp, root)
                for path in paths:
                    word = ''
                    for px, py in path:
                        word += self.board[px][py]
                        self.visited[px][py] = True
                    self.temp.append(word)
                    
                    if len(self.temp) > len(self.results):
                        self.results = self.temp[:]
                        
                    self.dfs(i, j, root)
                    self.temp.pop()
                    for px, py in path:
                        self.visited[px][py] = False
            y = 0
        
    # 以i，j为起点的所有单词可能
    def getAllPaths(self, i, j, paths, temp, root):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or \
            self.board[i][j] not in root.children or \
            self.visited[i][j] == True:
            return
       
        root = root.children[self.board[i][j]]
        if root.isWord:
            temp.append((i,j))
            paths.append(temp[:])
            temp.pop()
            return
            
        self.visited[i][j] = True
        deltas = [(0,1), (0,-1), (1,0), (-1, 0)]
        for dx, dy in deltas:
            newx = i + dx
            newy = j + dy
            temp.append((i,j))
            self.getAllPaths(newx, newy, paths, temp, root)
            temp.pop()
        self.visited[i][j] = False
