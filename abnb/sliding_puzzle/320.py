import Queue
import copy
class Solution:
    def getHash(self, matrix):
        res=0
        for arr in matrix:
            for t in arr:
                res=res*10+t
        return res
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """
    def getTarget2x3(self):
        return [
            [1, 2, 3],
            [4, 5, 0],
        ]

    def getTarget3x3(self):
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

    def  jigsawPuzzle(self, matrix):
        self.m=len(matrix)
        self.n=len(matrix[0])
        stateLookup={}
        target=self.getTarget3x3()
        targetHash=self.getHash(target)
        curHash=self.getHash(matrix)
        if targetHash==curHash:
            return 'YES'
        stateLookup[curHash]=0
        stateQueue=Queue.Queue()
        stateQueue.put(copy.deepcopy(matrix))
        directions=[(0, 1), (0, -1), (1, 0), (-1, 0)]

        while not stateQueue.empty():
            curState=stateQueue.get()
            step=stateLookup[self.getHash(curState)]
            # find 0
            shouldBreak=False
            for i in range(self.m):
                for j in range(self.n):
                    if curState[i][j]==0:
                        for dx, dy in directions:
                            newX=i+dx
                            newY=j+dy
                            if 0<=newX<self.m and 0<=newY<self.n:
                                newState=copy.deepcopy(curState)
                                newState[i][j], newState[newX][newY]=newState[newX][newY], newState[i][j]
                                newSatteHash=self.getHash(newState)
                                if newSatteHash not in stateLookup:
                                    if newSatteHash==targetHash:
                                        return "YES"
                                    else:
                                        stateLookup[newSatteHash]=step+1
                                        stateQueue.put(newState)
                        # it should be stopped
                        shouldBreak=True
                    if shouldBreak:
                        break
                if shouldBreak:
                    break

        return "NO"


matrix=[[1,2,3],[5,4,6],[7,8,0]]
s=Solution()
print s.jigsawPuzzle(matrix)
