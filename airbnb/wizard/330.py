from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for src, dst, cost in edges:
        if g.get(src) is None:
            g[src]=[]
        g[src].append((cost, dst))
    for k in g:
        print k, g[k]

    q=[(0, f, [])]
    seen=set()
    minLookup={f:0}

    while len(q)!=0:
        curCost, curNode, curPath=heappop(q)
        if curNode in seen:
            continue
        curPath.append(curNode)
        if curNode==t:
            return (curCost, curPath)
            
        nextList=g.get(curNode, [])
        for stepCost, nextNode in nextList:
            if nextNode in seen:
                continue
            oldNextNodeCost=minLookup.get(nextNode, None)
            newNextNodeCost=curCost+stepCost
            if oldNextNodeCost is None or newNextNodeCost<oldNextNodeCost:
                # should not add to seen
                minLookup[nextNode]=newNextNodeCost
                heappush(q, (newNextNodeCost, nextNode, curPath[:]))

            





if __name__ == "__main__":
    edges = [
        ("A", "B", 4),
        ("A", "C", 3),
        ("B", "C", 2),
        ("B", "D", 5),
        ("C", "D", 1),
    ]

    print "=== Dijkstra ==="
    print edges
    print dijkstra(edges, "A", "D")
