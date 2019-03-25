class Node:
    def __init__(self, a, b):
        self.a=a
        self.b=b

node1=Node(1, 100)
node2=Node(2, 80)
node3=Node(3, 90)

l=[node1, node2, node3]

rst=sorted(l, key=lambda x: x.a)
for v in rst:
    print v.a, ' ', v.b
