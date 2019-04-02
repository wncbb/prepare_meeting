
from collections import deque

def t(s, k):
    res=[]
    if len(s)<k or k<0:
        return
    q=deque()

    for i in range(len(s)):
        if len(q)>0:
            while i>=q[0]+k:
                q.popleft()

            while len(q)>0 and s[i]>=s[q[-1]]:
                q.pop()

        q.append(i)

        if i+1>=k:
            res.append(s[q[0]])


    return res

s=[2,3,4,2,6,2,5,1]
k=3
rst=t(s, k)
print rst





