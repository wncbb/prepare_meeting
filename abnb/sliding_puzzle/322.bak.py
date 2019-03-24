# -*- encoding: utf-8 -*-

from collections import deque
class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """
    def jigsawPuzzle(self, matrix):
        target = '123456780'
        start = ''
        for row in matrix:
            for n in row:
                start += str(n)

        directions = []
        for i in range(3):
            for j in range(3):
                d = []
                # 上下左右
                if i-1 >= 0: d.append((i-1)*3+j)
                if i+1 < 3: d.append((i+1)*3+j)
                if j-1 >= 0: d.append(i*3+j-1)
                if j+1 < 3: d.append(i*3+j+1)
                directions.append(d)

        print start
        print directions


        queue = deque()
        visted = set()
        queue.append(start)
        while len(queue) > 0:
            cur_board = queue.popleft()
            if cur_board == target: return "YES"

            zero_index = cur_board.index('0')
            for direction in directions[zero_index]:
                move_board = ''
                # 这个for循环就是为了交换字母
                for i in range(9):
                    if i == zero_index: move_board += cur_board[direction]
                    elif i == direction: move_board += '0'
                    else: move_board += cur_board[i]
                if move_board in visted: continue
                visted.add(move_board)
                queue.append(move_board)

        return "NO"

matrix=[[1,2,3],[5,4,6],[7,8,0]]
s=Solution()
print s.jigsawPuzzle(matrix)
