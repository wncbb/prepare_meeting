from heap import heapify, heappush, heappop

def buildGraph(words):
    graph={}
    for word in words:
        for c in word:
            graph[c]=set()
    
    for i in range(len(words)-1):
        for j in range(min(len(words[i]), len(words[j]))):
            if words[i][j]!=words[i+1][j]:
                graph[words[i][j]].add(words[i+1][j])
    return graph

def sortGraph(graph):
    indegree={
        node: 0
        for node in graph
    }
    for c in graph:
        for neighbor in graph[c]:
            indegree[neighbor]+=1
    
    q=[node for node in graph if indegree[node]==0]
    heapify(q)
     
    tpOrder=''

    while q:
        cur=heappop(q)
        tpOrder=tpOrder+cur

        for nc in graph[cur]:
            indegree[nc]=indegree[nc]-1
            if indegree[nc]==0:
                heappush(tpOrder, nc)

    if len(tpOrder)==len(graph):
        return True
    
    return False

    



    
    
