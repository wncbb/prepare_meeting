# -*- encoding: utf8 -*-

def t(s):
    res=''
    for v in s: 
        lpV=a(v)
        if res=='':
            res+=lpV
        else:
            res+='\n'
            res+=lpV
    return res

def a(s):
    res=''
    for v in s:
        tmpV=v[1:-1]
        if res=='':
            res+=tmpV
        else:
            res+='|'
            res+=tmpV

    return res


s=[
    ['John', 'Smith', 'john.smith@gmail.com', 'Los Angeles', '1'],
    ['Jane', 'Roberts', 'janer@msn.com', 'San Francisco, CA', '0'],
    ['Alexandra "Alex"', 'Menendez', 'alex.menendez@gmail.com', 'Miami', '1']
]



rst=t(s)
print rst
