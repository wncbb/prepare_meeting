import collections
class TrieNode:
    def __init__(self, value):
        self.value=value
        self.children=collections.defaultdict()
        self.isWord=False
    @classmethod
    def insert(cls, root, word):
        p=root
        for ch in word:
            child=p.children.get(ch)
            if child is None:
                child=TrieNode(ch)
                p.children[ch]=child
            p=child
        p.isWord=True
        p.word=word

class Solution:
    # @param {char[][]} board a list of lists of char
    # @param {str[]} words a list of string
    # @return {int} an integer
    def boggleGame(self, board, words):
        root=TrieNode('')
        for word in words:
            TrieNode.insert(root, word)
        self.board=board
        self.result=[]
        self.m=len(board)
        self.n=len(board[0])
        self.root=root

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited=[[False for _ in range(self.n)] for _ in range(self.m)]
                self.helper(i, j, visited, root, [])

        return len(self.result)


    def helper(self, i, j, visited, root, curResult):
        # should be or, not ||
        if i<0 or i>=self.m or j<0 or j>=self.n:
            return
        if visited[i][j]:
            return
        ch=self.board[i][j]
        child=root.children.get(ch)
        if child is None:
            return
        visited[i][j]=True

        if child.isWord:
            curResult.append(child.word)
            if len(curResult)>len(self.result):
                self.result=curResult

            for i1 in range(self.m):
                for j1 in range(self.n):
                    if visited[i1][j1]:
                        continue
                    self.helper(i1, j1, visited, self.root, curResult[:])
        else:
            dirs=[(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in dirs:
                x=i+dx
                y=j+dy
                self.helper(x, y, visited, child, curResult[:])
            visited[i][j]=False
