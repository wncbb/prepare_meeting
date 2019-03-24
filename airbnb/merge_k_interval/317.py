"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        data=[]
        for interval in intervals:
            for one in interval: 
                data.append(one)

        sorted(data, key=lambda o:o.start)

        res=[data[0]]
        for i in range(1, len(data)):
            lastRes=res[len(res)-1]
            cur=data[i]
            if lastRes.end>=cur.start:
                lastRes.end=max(lastRes.end, cur.end)
            else:
                res.append(cur)

        return res


s=Solution()
data=[
  [Interval(1,3),Interval(4,7),Interval(6,8)],
  [Interval(1,2),Interval(9,10)]
]

rst=s.mergeKSortedIntervalLists(data)
for item in rst:
    print item.start, item.end
