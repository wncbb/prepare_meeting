# -*- encoding: utf-8 -*-

import collections

# should be class, not def
class TrieNode:
    def __init__(self, value):
        self.value=value
        self.isWord=False
        self.children=collections.defaultdict()

    @classmethod
    def insert(cls, root, word):
        p=root
        for c in word:
            # should be .get(c), not [c]
            child=p.children.get(c)
            if child is None:
                child=TrieNode(c)
                p.children[c]=child
            p=child
        p.isWord=True
        p.word=word
    
    @classmethod
    def searchWord(cls, root, word):
        p=root
        for ch in word:
            child=p.children.get(ch)
            if child is None:
                return False
            p=child
        return p.isWord

    @classmethod
    def searchPrefix(cls, root, prefix):
        p=root
        for ch in prefix:
            child=p.children.get(ch)
            if child is None:
                return False
            p=child
        return True

class Solution:
    # @param {char[][]} board a list of lists of char
    # @param {str[]} words a list of string
    # @return {int} an integer
    def boggleGame(self, board, words):
        self.board=board
        self.m=len(board)
        self.n=len(board[0])
        self.result=0

        self.s=[]

        self.count=0

        # print "m:", self.m, " n:", self.n

        root=TrieNode('')
        for word in words:
            TrieNode.insert(root, word)

        self.root=root
        
        for i in range(self.m):
            for j in range(self.n):
                # m行， n列，大哥
                visited = [[False for _ in range(self.n)] for _ in range(self.m)]
                self.scan(i, j, root, visited, 0, [])

        return len(self.s)
        # return self.result

    def scan(self, i, j, node, visited, result, s):
        if visited[i][j]:
            return
        
        ch=self.board[i][j]
        if ch not in node.children:
            return
        
        visited[i][j]=True
        child=node.children.get(ch)

        if child.isWord:
            result=result+1
            s.append(child.word)
            if result>self.result:
                self.result=result
                # shoudl be s[:], not s
                self.s=s[:]
            
            for x in range(self.m):
                for y in range(self.n):
                    # print 'x:', x, ' y:', y
                    # print 'a:', len(visited), ' b:', len(visited[0])
                    if not visited[x][y]:
                        self.scan(x, y, self.root, visited, result, s)                        
            return

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if  (0 <= i + di < self.m and 0 <= j + dj < self.n) and not visited[i + di][j + dj]:
                self.scan(i + di, j + dj, child, visited, result, s)
        visited[i][j] = False


s=Solution()
board=[
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
words=["abc", "cfi", "beh", "defi", "gh"]

# board=["aaaa","aaaa","aaaa"]
# words={"aaa","aa","a","aaaa","aaaaa","aaaaaa"}

board=["abcdefg","huyuyww","ghihjui","wuiiuww"]
words={"efg","defi","gh","iuw","ww","iw","ghih","dasf","aaa"}

rst=s.boggleGame(board, words)
print rst
print s.count
