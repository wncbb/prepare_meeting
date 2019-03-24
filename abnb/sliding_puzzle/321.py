import collections
class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """
    def jigsawPuzzle(self, matrix):
        # convert states to string then bfs
        start, end = "", "123456780"
        for i in range(3):
            for j in range(3):
                start += str(matrix[i][j])
        visited, queue = set(start), collections.deque([start])
    
        while queue:
            state = queue.popleft()
            if state == end: return 'YES'
            for nextState in self.getNeighborStates(state):
                if not nextState in visited:
                    queue.append(nextState)
                    visited.add(nextState)
        return 'NO'
            
    def getNeighborStates(self, state):
        nextStates = []
        zeroPos = state.find('0')
        x, y = zeroPos/3,  zeroPos % 3
        
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3 : continue # not in range
            a, b = 3 * x + y, 3 * nx + ny
            newState = state[: a] + state[b] + state[a + 1:]
            newState = newState[: b] + '0' + newState[b + 1:]
            nextStates.append(newState)
    
        return nextStates

matrix=[[1,2,3],[5,4,6],[7,8,0]]
s=Solution()
print s.jigsawPuzzle(matrix)
