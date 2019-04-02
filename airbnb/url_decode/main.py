
def a(l, ch):
    if len(l)==0:
        if ch.isalpha():
            return [ch.upper(), ch.lower()]
        else:
            return [ch]
    res=[]
    if ch.isalpha():
        for s in l:
            res.append(s+ch.upper())
            res.append(s+ch.lower())
    else:
        for s in l:
            res.append(s+ch)

    return res

def t(s):
    res=[]
    for i, ch in enumerate(s):
        res=a(res, ch)
    return res



d='aBC'
rst=t(d)
for v in rst:
    print v
