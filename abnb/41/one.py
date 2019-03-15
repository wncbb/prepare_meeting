class Trie:
    def __init__(self):
        self.is_leaf = False
        self.word = None
        self.children = {}
        
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr =  curr.children[c]
        curr.is_leaf = True
        curr.word = word 
        
    def search(self, word):
        curr=self
        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return curr.is_leaf

    def is_prefix(self, word):
        curr=self
        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return True

class Solution(object):
    def findWords(self, board, words):
        m=len(board)
        if m==0:
            return []
        n=len(board[0])
        if n==0:
            return []

        trie=Trie()
        for word in words:
            trie.add(word)
        
        ret=set()

        def check(root, i, j, path):
            if root.is_leaf:
                ret.add(path)
                root.is_leaf=False
                return
            if i<0 or i>=m or j<0 or j>=n:
                return
            letter=board[i][j]
            if letter not in root.children:
                return
            board[i][j]='#'
            for r, c in((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                check(root.children[letter], r, c, path+letter)
            board[i][j]=letter


        for i in range(m):
            for j in range(n):
                check(trie, i, j, '')
        
        return list(ret)


s=Solution()
board=[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

word=["oath","pea","eat","rain"]
print s.findWords(board, word)