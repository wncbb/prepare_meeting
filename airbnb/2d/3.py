class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row=0
        self.col=0
        self.matrix=[]
        for v in vec2d:
            if len(v)==0:
                continue
            self.matrix.append(v)
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.hasNext():
            res=self.matrix[self.row][self.col]
            self.col+=1
            if self.col>=len(self.matrix[self.row]):
                self.col=0
                self.row+=1
            return res
        return 0


        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        if self.row<len(self.matrix) and self.col<len(self.matrix[self.row]):
            return True
        return False
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
