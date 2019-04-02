class TwoDIterator:
    def __init__(self, clist):
        self.l=[]
        for v in clist:
            self.l.extend(v)
        self.idx=-1
        self.removed=False
    def hasNext(self):
        self.idx+=1
        self.removed=False
        return self.idx<len(self.l)



    def next(self):
        if self.hasNext():
            return self.l[self.idx]
        return -1

    def remove(self):
        if self.removed:
            return
        self.l=self.l[0:self.idx]+self.l[self.idx+1:]
        self.removed=True
        self.idx-=1

clist = [[1,2,3],[4],[5]]
ti = TwoDIterator(clist)

print ti.next()
ti.remove()
print 'rl: ', ti.l
ti.remove()
print 'rl: ', ti.l
print ti.next()