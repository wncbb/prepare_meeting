
class UnionFind:
    def __init__(self, nodes):
        self.parents={}
        self.ranks={}
        for n in nodes:
            self.parents[n]=n
            self.ranks[n]=0
    
    def find(self, node):
        if node!=self.parents[node]:
            self.parents[node]=self.find(self.parents[node])
        return self.parents[node]

    def union(self, a, b):
        pa=self.find(a)
        pb=self.find(b)
        if pa==pb:
            return
        if self.ranks[pa]>self.ranks[pb]:
            self.parents[pb]=pa
        if self.ranks[pa]<self.ranks[pb]:
            self.parents[pa]=pb
        if self.ranks[pa]==self.ranks[pb]:
            self.parents[pb]=pa
            self.ranks[pa]+=1



def prim(edges):
    edges=sorted(edges, key=lambda x:x[0])
    nodes=set()
    for cost, src, dst in edges:
        nodes.add(src)
        nodes.add(dst)
    
    uf=UnionFind(nodes)

    res=[]

    for cost, src, dst in edges:
        if uf.find(src)==uf.find(dst):
            continue
        uf.union(src, dst)
        res.append([cost, src, dst])

    return res




edges=[
    (8, 'A', 'B'),
    (6, 'A', 'C'),
    (3, 'C', 'D'),
    (4, 'B', 'D'),
    (5, 'A', 'D')
]
rst=prim(edges)
for v in rst:
    print v