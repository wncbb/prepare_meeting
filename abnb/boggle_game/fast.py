class TrieNode(object):
    
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.word = None
        self.is_leaf = False
        
        
    def add_child(self, child):
        if child not in self.children:
            self.children[child] = TrieNode(child)
        return self.children[child]
        
    def get_child(self, child):
        return self.children.get(child, None)
        
    def build_tree(self, word):
        node = self
        for w in word:
            node = node.add_child(w)
        node.is_leaf = True
        node.word = word
        return


class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """
    def boggleGame(self, board, words):
        # write your code here
        from collections import defaultdict, deque
        def scan(i, j, node, visit, cnt):

            # if i < 0 or i >= len(board):
            #     return
            # if j < 0 or j >= len(board[i]):
            #     return

            if visit[i][j]:
                return
            ch = board[i][j]
            if ch not in node.children:
                return

            visit[i][j] = 1
            child = node.children[ch]
            if child.is_leaf:
                cnt += 1
                self.res = max(self.res, cnt)
                for x in range(len(board)):
                    for y in range(len(board[0])):
                        if not visit[x][y]:
                            scan(x, y, root, visit, cnt)

                # self.visit[i][j] = 0
                # cnt -= 1
                return
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not (0 <= i + di < rowNum and 0 <= j + dj < colNum) or visit[i + di][j + dj]:
                    continue
                scan(i + di, j + dj, child, visit, cnt)
            visit[i][j] = 0

        root = TrieNode("")
        for word in words:
            root.build_tree(word)
        rowNum, colNum = len(board), len(board[0])
        self.res = 0
        for i in range(rowNum):
            for j in range(colNum):
                visit = [[0 for _ in range(colNum)] for _ in range(rowNum)]
                scan(i, j, root, visit, 0)
        
        
        return self.res


s=Solution()
board=["aaaa","aaaa","aaaa"]
words={"aaa","aa","a","aaaa","aaaaa","aaaaaa"}
rst=s.boggleGame(board, words)
print rst
