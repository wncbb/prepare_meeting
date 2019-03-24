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

            # 要么向左移动
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

# 另一种写法, 调换了左右方向判断位置, 使代码更简洁

class Solution:
    """
    @param heights: the height of the terrain
    @param V: the units of water
    @param K: the index
    @return: how much water is at each index
    """
    def pourWater(self, heights, V, K):
        N = len(heights)
        for v in range(V):
            pos = K
            for i in range(K + 1, N):
                if heights[i] < heights[i - 1]:
                    pos = i
                elif heights[i] > heights[i - 1]:
                    break
            for i in range(K - 1, -1, -1):
                if heights[i] < heights[i + 1]:
                    pos = i
                elif heights[i] > heights[i + 1]:
                    break
            heights[pos] += 1
        return heights
