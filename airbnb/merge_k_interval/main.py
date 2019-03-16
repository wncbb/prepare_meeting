"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
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
        arr = sorted(arr, key=lambda o: o[0])
        ans = []
        if (len(arr) == 0) :
            return ans
        ans.append(arr[0])
        for i in range(1, len(arr)):
            if (ans[len(ans) - 1][1] >= arr[i][0]):
                ans[len(ans) - 1] = (ans[len(ans)-1][0], max(ans[len(ans) - 1][1], arr[i][1]))
            else :
                ans.append(arr[i])
        return ans


s=Solution()
data=[
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]

rst=s.mergeKSortedIntervalLists(data)
print rst
