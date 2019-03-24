class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.result = []
        for e in vec2d:
            self.result.extend(e)
        self.n = len(self.result)
        self.idx = 0
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        elem = self.result[self.idx]
        self.idx += 1
        return elem
        
        
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.idx < self.n:
            return True
        else:
            return False
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
