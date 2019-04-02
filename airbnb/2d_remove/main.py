class TwoDIterator:
  def __init__(self, clist):
        self.clist = clist
        self.rowId = 0
        self.colId = 0
        self.flag = True
        
        
  def hasNext(self):
      """
      self.rowId, self.colId
      """
      nrow = len(self.clist)
      while self.rowId<nrow and self.colId==len(self.clist[self.rowId]):
          self.rowId+=1
          self.colId=0
      return self.rowId<nrow

  def next(self):
      self.hasNext()
      ret = self.clist[self.rowId][self.colId]
      self.colId+=1
      self.flag = True
      return ret
      
  def remove(self):
      if not self.flag:
          return
      rowrm, colrm = self.rowId, self.colId
      # print rowrm,colrm
      # self.colId==0 can never happen
      colrm-=1
      del self.clist[rowrm][colrm]

      if not self.clist[rowrm]:
          del self.clist[rowrm]
          # no need to adjust rowId, as I am still pointing to the old rowId
          self.colId=0 
      else:
        self.colId-=1
      self.flag = False
      # print self.rowId,self.colId

clist = [[1,2,3],[4],[5]]
ti = TwoDIterator(clist)

print ti.next()
ti.remove()
ti.remove()
print ti.clist
print ti.next()
