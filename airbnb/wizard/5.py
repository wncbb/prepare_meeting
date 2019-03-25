from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    for k in g:
        print '-----------'
        print 'k:', k, ', v:', g[k]
        print '==========='

    # qsm
    # cnp
    q, seen, mins = [(0,f,[])], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path.append(v1)
            print 'v1:', v1, ' ,path:', path
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, []):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    # should be path[:], not path
                    heappush(q, (next, v2, path[:]))

    return float("inf")

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
