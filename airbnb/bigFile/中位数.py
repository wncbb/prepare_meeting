from heapq import *


class MedianFinder:
    def __init__(self):
        self.small=[]
        self.large=[]
    
    def add(self, num):
        heappush(self.large, num)
        heappush(self.small, -1*heappop(self.large))
        if len(self.large)<len(self.small):
            heappush(self.large, -1*heappop(self.small))

    def findMedian(self):
        if len(self.large)>len(self.small):
            return self.large[0]
        else:
            return (self.large[0]-self.small[0])/2.0

    
m=MedianFinder()
m.add(1)
print m.small, m.large, m.findMedian()
m.add(2)
print m.small, m.large, m.findMedian()
m.add(3)
print m.small, m.large, m.findMedian()