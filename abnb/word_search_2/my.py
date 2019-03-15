# -*- encoding: utf-8 -*-
import collections

"""
1. x,y i,j该用哪一个
2. self.board, not board
3. insert的最后isWord=True
4. range(len(board)) not range(board)
"""

class TrieNode(object):
    def __init__(self, value):
        self.isWord=False
        self.value=value
        self.children=collections.OrderedDict()

    @classmethod
    def insert(cls, root, word):
        p=root
        for c in word:
            child=p.children.get(c)
            if child is None:
                child=TrieNode(c)
                p.children[c]=child
            p=child
        child.isWord=True

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if len(board)==0:
            return []
        # write your code here
        self.board=board
        self.words=words
        self.ret=set()

        root=TrieNode('')
        for word in words:
            root.insert(root, word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.findWords(i, j, root, '')

        return list(self.ret)


    # 从i,j位置的字母开始，但是现在还不算它
    def findWords(self, x, y, root, pre):
        if root.isWord:
            self.ret.add(pre)

        if x<0 or x>=len(self.board) or y<0 or y>=len(self.board[0]):
            return
        
        if self.board[x][y]=='#':
            return

        curNode=root.children.get(self.board[x][y])
        if curNode is None:
            return


        directions=[(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            nx=x+dx
            ny=y+dy
            oldChar=self.board[x][y]
            self.board[x][y]='#'

            self.findWords(nx, ny, curNode, pre+oldChar)

            self.board[x][y]=oldChar


s=Solution()
words=['oath','pea','eat','rain']
board=[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

#Output: ["eat","oath"]

print s.wordSearchII(board, words)



"""
Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'], ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]

"""



"""
words=['abc', 'abm', 'cad']

root=TrieNode('')

for word in words:
    TrieNode.insert(root, word)

print dict(root.children)
"""
