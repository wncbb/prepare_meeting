graph={
    "A": ["B", "C"],
    "C": ["D"]
}

def BFS(graph, s):
    queue=[]
    queue.append(s)
    seen=set()
    seen.add(s)
    parent={s: None}

    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w]=vertex
    return parent
