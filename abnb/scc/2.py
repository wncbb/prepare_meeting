import collections

def kosaraju(g1, g2):
    nodes=set(g1.keys())|set(g2.keys())
    stack=[]

    visited=set()
    def visit(node):
        if node in visited:
            return
        visited.add(node)
        for nextNode in g1.get(node, set()):
            visit(node)
        stack.append(node)

    for node in nodes:
        visit(node)

    visited=set()
    def visitV2(node, tmp):
        if node in visited:
            return

        visited.add(node)
        for nextNode in g2.get(node, set()):
            visitV2(nextNode, tmp)
        tmp.add(node)
        stack.append(node)

    scc=[]
    while len(stack)>0:
        tmp=set()
        node=stack.pop()
        visitV2(node, tmp)
        if len(tmp)>0:
            scc.append(tmp)
    print scc

    lookup={}
    for sc in scc:
        k=max(sc)
        for c in sc:
            lookup[c]=k

    gg=collections.defaultdict(set)
    
    for s in g1:
        children=g1.get(s, set())
        for child in children:
            print s, child
            gg[lookup[s]].add(lookup[child])
    print gg
            

def leastNodes(edges):
    graphA=collections.defaultdict(set)
    graphB=collections.defaultdict(set)
    for s, d in edges:
        graphA[s].add(d)
        graphB[d].add(s)
    
    kosaraju(graphA, graphB)


s=[(0, 1), (1, 2), (2, 3), (4, 5)]
# s=[(0, 1), (1, 0), (2, 3), (3, 2), (2, 1)]
rst=leastNodes(s)
print rst
