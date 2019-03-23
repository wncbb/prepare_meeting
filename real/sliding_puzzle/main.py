from collections import deque
class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """

    def getTarget(self):
        return [
            [1, 2, 3],
            [4, 5, 0]
        ]

    def matrix2string(self, matrix):
        res=''
        for row in matrix:
            for num in row:
                res=res+str(num)
        return res

    def slidingPuzzle(self, matrix):
        self.m=len(matrix)
        self.n=len(matrix[0])
        self.target=self.matrix2string(self.getTarget())
        curState=self.matrix2string(matrix)
        if curState==self.target:
            return "YES"

        pos2dirs=[
            [1, 3], # 0
            [0, 2, 4], # 1
            [1, 5], # 2
            [0, 4], # 3
            [1, 3, 5], # 4
            [2, 4], # 5
        ]

        q=deque()
        q.append((curState, 0))
        visited=set()
        visited.add(curState)

        while len(q)!=0:
            curState, step=q.popleft()

            if curState==self.target:
                return step

            zeroIdx=curState.index('0')
            dirs=pos2dirs[zeroIdx]
            for exPos in dirs:
                newState=self.exchangeStrPos(curState, zeroIdx, exPos)
                if newState==self.target:
                    return step+1
                elif newState not in visited:
                    q.append((newState, step+1))
                    visited.add(newState)
        return -1


    def exchangeStrPos(self, s, i, j):
        res=''
        for x in range(len(s)):
            if x==i:
                res+=s[j]
            elif x==j:
                res+=s[i]
            else:
                res+=s[x]
        return res
