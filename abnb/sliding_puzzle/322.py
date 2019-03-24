from collections import deque
class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """

    def getTarget(self):
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

    def matrix2string(self, matrix):
        res=''
        for row in matrix:
            for num in row:
                res=res+str(num)
        return res

    def jigsawPuzzle(self, matrix):
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
            [0, 4, 6], # 3
            [1, 3, 5, 7], # 4
            [2, 4, 8], # 5
            [3, 7], # 6
            [4, 6, 8], # 7
            [5, 7], # 8
        ]

        stack=[curState]
        states=set()
        states.add(curState)

        while len(stack)!=0:
            curState=stack.pop()
            if curState==self.target:
                return "YES"

            zeroIdx=curState.index('0')
            dirs=pos2dirs[zeroIdx]
            for exPos in dirs:
                newState=self.exchangeStrPos(curState, zeroIdx, exPos)
                if newState==self.target:
                    return 'YES'
                if newState not in states:
                    states.add(newState)
                    stack.append(newState)
        return 'NO'
               

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
                





matrix=[[1,2,3],[5,4,6],[7,8,0]]
s=Solution()
print s.exchangeStrPos('012345', 0, 5)
print s.jigsawPuzzle(matrix)






