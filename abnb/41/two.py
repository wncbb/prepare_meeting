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
    
        
    # def is_prefix(self, prefix):
    #     curr:=self.root
    #     for c in prefix:
    #         curr=curr.children.get(c)
    #         if curr is None:
    #             return False

    #     return True
    # def search(self, word):
    #     curr=self.root
    #     for c in root:
    #         curr=curr.children.get(c)
    #         if c is None:
    #             return False
    #     return currr.is_word

def dfs(board, i, j, m, n, trie):
    res=set()
    if 0<=i<=m-1 and 0<=j<=n-1 and board[i][j]!='#':
        tmp=board[i][j]
        board[i][j]='#'
        if trie.is_leaf:
            res.add(trie.word)
            trie.is_leaf=False
        if tmp not in trie.children:
            return set()
        for r, c in((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            part_set=dfs(board, r, c, m, n, trie.children[tmp])
            res|=part_set
        board[i][j]=tmp
    return res

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

        for i in range(m):
            for j in range(n):
                ret|=dfs(board, i, j, m, n, trie)
        
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