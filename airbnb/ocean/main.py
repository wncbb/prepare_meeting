import collections
s=[
    ['W', 'W', 'W', 'L', 'L', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'L', 'W', 'W'],
    ['W', 'L', 'L', 'L', 'L', 'W', 'W']
]

def t2(s, x, y):
    q=collections.deque()
    q.append((x, y))
    dirs=[(0,1), (0,-1), (1,0), (-1,0)]

    while len(q)>0:
        curx, cury=q.pop()
        if s[curx][cury]!='W':
            continue
        s[curx][cury]='O'
        for dx, dy in dirs:
            nx=curx+dx
            ny=cury+dy
            if nx<0 or nx>= len(s) or ny<0 or ny>=len(s[0]):
                continue
            if s[nx][ny]=='W':
                q.append((nx, ny))



def t(s, x, y):
    if x<0 or x>= len(s) or y<0 or y>=len(s[0]):
        return
    dirs=[(0,1), (0,-1), (1,0), (-1,0)]
    print 'x', x, 'y', y
    if s[x][y]!='W':
        return
    s[x][y]='O'
    for dx, dy in dirs:
        nx=x+dx
        ny=y+dy
        t(s, nx, ny)

# t(s, 0, 1)
# for v in s:
#     print v


t2(s, 0, 1)
for v in s:
    print v