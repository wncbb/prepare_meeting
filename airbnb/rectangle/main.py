
def isOverlapping(a, b):
    a0x=a[0][0]
    a1x=a[1][0]
    a0y=a[0][1]
    a1y=a[1][1]

    b0x=b[0][0]
    b1x=b[1][0]
    b0y=b[0][1]
    b1y=b[1][1]

    if (a0x>b1x or a1x<b0x) or (a0y>b1y or a1y<b0y):
        return False
    return True

def rectangleOverlapping(rects):
    num=len(rects)

    parentLookup=range(num)

    def findParent(a):
        if parentLookup[a]!=a:
            parentLookup[a]=findParent(parentLookup[a])
        return parentLookup[a]

    def union(a, b):
        parentA=findParent(a)
        parentB=findParent(b)
        if parentA!=parentB:
            parentLookup[parentA]=parentB
            return 1
        return 0

    res=num
    for i in range(num):
        for j in range(i+1, num):
            if isOverlapping(rects[i], rects[j]):
                res-=union(i, j)
    
    return res


s=[
    [(0,0),(2,2)],
    [(1,1),(3,3)],
    [(1,0),(3,4)]
]
s=[
    [(0,0),(2,2)],
    [(1,1),(3,3)],
    [(4,4),(6,6)],
    [(5,5),(7,7)]
]

# rst=rectangleOverlapping(s)
# print rst

print isOverlapping([(0, 0), (3, 3)], [(1, 1), (2, 2)])
