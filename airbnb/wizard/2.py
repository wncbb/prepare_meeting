from collections import defaultdict
from heapq import *

# 前三名 吹牛皮

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    # q, seen, mins
    # qsm
    # cost, source, path
    # cost, node, path
    # cnp
    q, seen, mins = [(0,f,[])], set(), {f: 0}
    parent={}
    while q:
        (cost,v1,path) = heappop(q)
        print 'LINE18 cost', cost, 'v1', v1, 'path', path
        if v1 not in seen:
            seen.add(v1)
            # should path.append(v1)
            # not path=path.append(v1)
            print 'LINE22', 'path', path, 'v1', v1
            path.append(v1)
            print 'parent', parent
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                print 'LINE29', 'v2', v2, 'v1', v1, 'path', path
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    parent[v2]=v1
                    mins[v2] = next
                     #print 'next', next, 'v2', v2, 'path', path
                    heappush(q, (next, v2, path[:]))
    
    return float("inf")

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
    print "A -> F:"
    print dijkstra(edges, "A", "F")
    # print "F -> G:"
    # print dijkstra(edges, "F", "G")
