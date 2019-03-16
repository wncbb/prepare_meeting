# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        arr = []
        for i in intervals:
            for j in i:
                arr.append(j)
        arr = sorted(arr, key=lambda o: o.start)
        ans = []
        if (len(arr) == 0) :
            return ans 
        ans.append(arr[0])
        for i in range(1, len(arr)):
            if (ans[len(ans) - 1].end >= arr[i].start):
                ans[len(ans) - 1].end = max(ans[len(ans) - 1].end, arr[i].end)
            else :
                ans.append(arr[i])
        return ans
