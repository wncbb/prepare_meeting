class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.list=[]
        for v in vec2d:
            self.list.extend(v)
        self.idx=0
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.hasNext():
            res=self.list[self.idx]
            self.idx+=1
            return res
        return 0

        
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        return self.idx<len(self.list)
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

