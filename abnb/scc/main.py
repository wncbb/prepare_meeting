import collections


def leastNodes(edges):
    pred=collections.defaultdict(set)
    succ=collections.defaultdict(set)

    for start, end in edges:
        # end -> start
        pred[end].add(start)
        # start -> end
        succ[start].add(end)
    
    components=kosarajus(pred, succ)
    component_succ=collections.defaultdict(set)
    component_pred=collections.defaultdict(set)

    for start, end in edges:
        if components[start]!=components[end]:
            component_start=components[start]
            component_end=components[end]

            component_succ[component_start].add(component_end)
            component_pred[component_end].add(component_start)

    print 'component_succ: ', component_succ
    print 'component_pred: ', component_pred
    
    return set(component_succ.keys())-set(component_pred.keys())

def kosarajus(pred, succ):
    all_nodes=set(pred.keys())|set(succ.keys())
    order=[]
    visited=set()
    def visit(node):
        if node not in visited:
            visited.add(node)
            # start -> end
            for out_neighbor in succ[node]:
                visit(out_neighbor)
            order.append(node)

    for node in all_nodes:
        visit(node)
    
    print 'order: ', order

    components={}

    def assign(node, root):
        print 'node:', node, 'root:', root
        if node not in components:
            components[node]=root
            # end -> start
            for in_neighbor in pred[node]:
                # start, end
                assign(in_neighbor, root)
                
    while len(order)>0:
        tmp=[]
        node=order.pop()
        assign(node, node)
    print 'components: ', components
    return components

# s=[(0, 1), (1, 2), (2, 0), (0, 3), (0, 4)]
s=[(0, 1), (1, 2), (2, 3), (4, 5), (6, 6)]
rst=leastNodes(s)
print rst