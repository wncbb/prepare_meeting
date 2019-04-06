from heapq import *
import math

graph=[
    'A': {'B': 10},
]

def init_distance(graph, s):
    distance={s:0}
    for vertex in graph:
        if vertex!=s:
            distance[vertex]=math.inf
    return distance

def dijkastra(graph , s):
    pqueue=[]
    heappush(pqueue, (0, s))
    seen=set()
    parent={s: None}
    distance=init_distance(graph, s)

    while(len(pqueue))>0:
        dist, vertex=vertex heappop(pqueue)
        seen.add(vertex)

        nodes=graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                newDist=dist+graph[vertex][w]
                if newDist < distance[w]:
                    parent[w]=vertex
                    distance[w]=newDist
                    heappush(pqueue, (newDist, w))
    
    
    return parent, distance