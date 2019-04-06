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
        ("A", "B", 5),
        ("A", "C", 1),
        ("B", "C", 2),
        ("B", "D", 1),
        ("C", "D", 4),
        ("C", "E", 8),
        ("D", "E", 3),
        ("D", "F", 6),

        ("B", "A", 5),
        ("C", "A", 1),
        ("C", "B", 2),
        ("D", "B", 1),
        ("D", "C", 4),
        ("E", "C", 8),
        ("E", "D", 3),
        ("F", "D", 6),

    ]

    print "=== Dijkstra ==="
    print edges
    print dijkstra(edges, "A", "F")
