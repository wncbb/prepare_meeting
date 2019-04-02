# -*- encoding: utf-8 -*-

# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    """
    @param heights: the height of the terrain
    @param V: the units of water
    @param K: the index
    @return: how much water is at each index
    """

    def pourWater(self, heights, V, K):
        for _ in range(V):
            index = -1
            for i in range(K-1, -1, -1):
                if heights[i] > heights[i+1]:
                    break
                elif heights[i] < heights[i+1]:
                    index = i
            if index != -1:
                heights[index] += 1
                continue
            
            # 要么向右移动
            index = -1
            for i in range(K+1, len(heights)):
                if heights[i] > heights[i-1]:
                    break
                elif heights[i] < heights[i-1]:
                    index = i
            if index != -1:
                heights[index] += 1
                continue

            # 要么待在原地
            heights[K] += 1
        return heights
heights = [2,1,1,2,1,2,2]
V = 4
K = 3
s=Solution()
rst=s.pourWater(heights, V, K)
print rst
