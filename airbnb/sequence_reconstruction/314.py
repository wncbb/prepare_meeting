# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

class Solution:
    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org
            
    def build_graph(self, seqs):
        graph={}
        for seq in seqs:
            for i in range(1, len(seq)):
                prv=seq[i-1]
                nxt=seq[i]
                if prv not in graph:
                    graph[prv]=set()
                graph[prv].add(nxt)
        return graph
    
    def get_indegrees(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
                
        return indegrees
        
    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)
        
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        
        topo_order = []
        while queue:
            if len(queue) > 1:
                # there must exist more than one topo orders
                return None
                
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) == len(graph):
            return topo_order
            
        return None

s=Solution()
seqs=[
        [1, 2, 3],
        [2, 3, 4],
]
rst=s.build_graph(seqs)
print rst


