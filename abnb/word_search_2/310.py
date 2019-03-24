# -*- encoding: utf-8 -*-

import collections

class TrieNode:
    def __init__(self, value):
        self.isWord=False
        self.value=value
        self.children=collections.OrderedDict()

    # don't forget @classmethod
    @classmethod
    def insert(cls, root, word):
        p=root
        for ch in word:
            # should be p.children.get not p.get
            child=p.children.get(ch)
            if child is None:
                child=TrieNode(ch)
                # should be p.children[ch], not p[ch]
                p.children[ch]=child
            p=child
        # 必须设置isWord
        p.isWord=True    
        

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        # TODO: check params
        self.board=board
        trieRoot=TrieNode('')
        for word in words:
            TrieNode.insert(trieRoot, word)
        self.result=set()
        # should be range(len(self.board)), not len(self.board)
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                # should be self.dfs, not dfs
                self.dfs(i, j, trieRoot, '')
        return list(self.result)
        
    def dfs(self, i, j, trieNode, preStr):
        if i<0 or i>=len(self.board) or j<0 or j>=len(self.board[0]):
            return
        if self.board[i][j]=='#':
            return
        curNode=trieNode.children.get(self.board[i][j])
        if curNode is None:
            return

        curStr=preStr+self.board[i][j]
        if curNode.isWord:
            self.result.add(curStr)

        dirs=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        oldCh=self.board[i][j]
        for dx, dy in dirs:
            x=i+dx
            y=j+dy
            self.board[i][j]='#'
            self.dfs(x, y, curNode, curStr)
            self.board[i][j]=oldCh




# words=['abc', 'abd', 'cbd']
# root=TrieNode('')
# for word in words:
#     TrieNode.insert(root, word)
# print dict(root.children)
board=[
    ['d', 'o', 'a', 'f'],
    ['a', 'g', 'a', 'i'],
    ['d', 'c', 'a', 'n'],
]
words=["doa", "dog", "dad", "dgdg", "can", "again"]
s=Solution()
print s.wordSearchII(board, words)
