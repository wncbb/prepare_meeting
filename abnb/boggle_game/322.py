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
        self.num=0
        self.m=len(board)
        self.n=len(board[0])
        self.root=root

        for i in range(self.m):
            for j in range(self.n):
                visited=[[False for _ in range(self.n)] for _ in range(self.m)]
                self.helper(i, j, root, visited, [], 0)

        print self.result
        return len(self.result)


    def helper(self, i, j, root, visited, curResult, curNum):
        if visited[i][j]:
            return

        ch=self.board[i][j]
        child=root.children.get(ch)
        if child is None:
            return

        visited[i][j]=True

        if child.isWord:
            curResult.append(child.word)
            curNum+=1
            # if len(curResult)>len(self.result):
            print '1111111111111'
            print curNum
            print curResult
            print '2222222222222'
            # if curNum>self.num:
            if len(curResult)>len(self.result):
                self.result=curResult[:] 
                self.num=curNum

            # for i1 in range(self.m):
            #     for j1 in range(self.n):
            #         if not visited[i1][j1]:
            #             self.helper(i1, j1, visited, self.root, curResult)
            # return
            for x in range(self.m):
                for y in range(self.n):
                    # print 'x:', x, ' y:', y
                    # print 'a:', len(visited), ' b:', len(visited[0])
                    if not visited[x][y]:
                        self.helper(x, y, self.root, visited, curResult[:], curNum)                        
            return
        
        # dirs=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        # for dx, dy in dirs:
        #     x=i+dx
        #     y=j+dy
        #     self.helper(x, y, visited, child, curResult)
        # visited[i][j]=False
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if  (0 <= i + di < self.m and 0 <= j + dj < self.n) and not visited[i + di][j + dj]:
                self.helper(i + di, j + dj, child, visited, curResult, curNum)
        # TODO: so important
        visited[i][j] = False


s=Solution()
# board=[['a', 'b', 'c'],
#    ['d', 'e', 'f'],
#    ['g', 'h', 'i']]
# words=["abc", "cfi", "beh", "defi", "gh"]

#board=["aaaa","aaaa","aaaa","aaaa"]
# words={"a"}
board=["abcdefg","huyuyww","ghihjui","wuiiuww"]
words={"efg","defi","gh","iuw","ww","iw","ghih","dasf","aaa"}
rst=s.boggleGame(board, words)
print rst
