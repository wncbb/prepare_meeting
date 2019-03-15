# -*- encoding: utf-8 -*-
import collections
import os
class TrieNode(object):
    def __init__(self, value):
        self.value=value
        self.isWord=False
        self.children=collections.OrderedDict()

    @classmethod
    def insert(cls, root, word):
        p=root
        for c in word:
            child=p.children.get(c)
            if not child:
                child=TrieNode(c)
            p.children[c]=child
            p=child
        p.isWord=True

class Solution:
    def boggleGame(self, board, words):
        self.board=board
        self.words=words
        self.m=len(board)
        self.n=len(board[0])

        self.results=[]
        self.tmp=[]

        self.visited=[[False for _ in xrange(self.n)] for _ in xrange(self.m)]

        self.root=TrieNode('')
        for word in words:
            TrieNode.insert(self.root, word)

        self.tryPosition(0, 0, self.root)
        return len(self.results)

    def tryPosition(self, x, y, root):
        print "x:", x, " y:", y
        for i in xrange(x, self.m):
            for j in xrange(y, self.n):
                paths=[]
                tmp=[]
                self.findWords(i, j, root, paths, tmp)

                # print('i:{}, j:{} \n'.format(i, j))
                # print paths
                # print tmp
                # print dict(root.children)
                # print '-------------\n'
                # # os._exit(1)
                # print "paths:", paths
                # print "tmp:", tmp
                # os._exit(1)

                for path in paths:
                    word=''
                    for px, py in path:
                        word+=self.board[px][py]
                        self.visited[px][py]=True

                    self.tmp.append(word)
                    if len(self.tmp)>len(self.results):
                        self.results=self.tmp[:]
                    
                    self.tryPosition(i, j, root)
                    self.tmp.pop()

                    for px, py in path:
                        self.visited[px][py]=False

            y=0

    # find all valid words from the beginning of i,j
    def findWords(self, i, j, root, paths, tmp):
        # tmp记录的是当前的路径
        print i, j, paths, tmp
        if i<0 or j<0 or i>=self.m or j>=self.n or self.visited[i][j]==True:
            # print '75'
            return
        # 看当前的字母在不在当前这一层Trie树中，如果不在，就没必要继续了
        if self.board[i][j] not in root.children:
            # print '79'
            return 

        root=root.children[self.board[i][j]]
        if root.isWord:
            tmp.append((i, j))
            # TODO: 
            paths.append(tmp[:])
            tmp.pop()
            return

        directions=[
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        
        self.visited[i][j]=True
        for dx, dy in directions:
            x=i+dx
            y=j+dy
            # TODO: (i, j), not (x, y)
            tmp.append((i, j))
            self.findWords(x, y, root, paths, tmp)
            tmp.pop()

        self.visited[i][j]=False



s=Solution()
board=[
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

# d = ["abc", "fci", "beh", "defi", "gh"]
d = ["abc", "adg", "beh", "defi", "gh"]

print s.boggleGame(board, d)