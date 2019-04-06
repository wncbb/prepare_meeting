
def isOverlapping(a, b):
    ax0=a[0][0]
    ax1=a[1][0]
    ay0=a[0][1]
    ay1=a[1][1]

    bx0=b[0][0]
    bx1=b[1][0]
    by0=b[0][1]
    by1=b[1][1]

    if (ax0>bx1 or ax1<bx0) or (ay0>by1 or ay1<by0):
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

rst=rectangleOverlapping(s)
print rst

