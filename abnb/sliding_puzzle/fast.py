import Queue
import copy
class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """
    def hash(self, matrix):
        t = 0
        for i in matrix:
            for j in i:
                t = t * 10 + j
        return t
    def bfs(self, matrix, ans):
        if matrix == ans :
            return 0
        dis = {}
        move = [[0,1],[0,-1],[1,0],[-1,0]]
        q = Queue.Queue()
        q.put(matrix)
        dis[self.hash(matrix)] = 0
        while not q.empty():
            state = q.get()
            step = dis[self.hash(state)]
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 0:
                        for k in range(4):
                            ti = i + move[k][0]
                            tj = j + move[k][1]
                            if ti >= 0 and ti < 3 and tj >= 0 and tj < 3:
                                newstate = copy.deepcopy(state)
                                newstate[i][j], newstate[ti][tj] = newstate[ti][tj], newstate[i][j]
                                if self.hash(newstate) not in dis:
                                    if(self.hash(newstate) == self.hash(ans)):
                                        return "YES"
                                    dis[self.hash(newstate)] = step + 1
                                    q.put(newstate)
                        break
        return "NO"
                    
    def  jigsawPuzzle(self, matrix):
        # Write your code here
        ans = [[1,2,3],[4,5,6],[7,8,0]]
        return self.bfs(matrix, ans)

matrix=[
[1,2,3],
[4,5,6],
[7,0,8]
]
s=Solution()
print s.jigsawPuzzle(matrix)





