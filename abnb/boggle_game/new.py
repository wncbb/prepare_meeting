class TrieNode:
  def __init__(self):
    self.isWord = False
    self.neighbor = [None]*26

class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, word):
    def helper(idx, word, root):
      if idx==len(word):
        root.isWord = True
        return
      
      c = word[idx]
      nidx = ord(c)-ord('a')
      if root.neighbor[nidx] is None:
        root.neighbor[nidx] = TrieNode()
      
      helper(idx+1, word, root.neighbor[nidx])
    
    helper(0, word, self.root)

# return indices of found words
def findwords(root, board, x, y):
  """
  find indices of matching words from a point
  """
  m,n=len(board),len(board[0])
  dirs = [(1,0),(0,1),(0,-1),(-1,0)]
  def helper(root, board, x, y, indices, allindices):
    if x>=m or x<0 or y>=n or y<0 or board[x][y]=='#':
      return

    c = board[x][y]
    idx = ord(c)-ord('a')
    if root.neighbor[idx] is None:
      return

    root = root.neighbor[idx]
    indices.append((x,y))
    if root.isWord:
      allindices.append(list(indices))

    board[x][y]='#'
    for d in dirs:
      x0,y0 = x+d[0],y+d[1]
      helper(root, board, x0,y0, indices, allindices)
    board[x][y]=c
    indices.pop()
  
  allindices = []
  indices = []
  helper(root, board, x, y, indices, allindices)
  return allindices

maxres = []

def bogglegame(board, worddict):
  """
  
  """
  m,n = len(board),len(board[0])
  trie = Trie()
  for w in worddict:
    trie.insert(w)

  def dfs(board, pos):
    """
    return max solution from the current points
    """
    if pos==m*n:
      return []

    maxres = []
    for p in range(pos, m*n):
      x,y=p/n,p%n
      allindices = findwords(trie.root, board, x, y)
      # print p, allindices
      for indices in allindices:
        wlist = []
        for i,j in indices:
          wlist.append(board[i][j])
          board[i][j]='#'

        res = dfs(board, pos+1)
        # print p, res
        if len(res)+1>len(maxres):
          maxres = [''.join(wlist)]+res

        # restore
        for k,c in enumerate(wlist):
          i,j=indices[k]
          board[i][j]=c
    return maxres
  
  return dfs(board, 0)