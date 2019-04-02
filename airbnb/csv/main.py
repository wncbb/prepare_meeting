csv_lines = [
  'John,Smith,john.smith@gmail.com,Los Angeles,10',
  'Jane,Roberts,janer@msn.com,"San Francisco, CA",0',
  '"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1',
  '1,2,,4,"5"',
  'aa,bb,"aa","aa,bb","aa""aa"""'
]

def parseT(line):
    res=[]
    isQuote=False
    token=''
    i=0
    while i<len(line):
        s=line[i]
        if s=='"':
            if isQuote:
                if i<len(line)-1 and line[i+1]=='"':
                    token+='"'
                    i=i+1
                elif i<len(line)-1 and line[i+1]==',':
                    res.append(token)
                    isQuote=False
                    token=''
                    i=i+1
                else:
                    token+='"'
            else:
                isQuote=True
        else:
            if isQuote:
                token+=s
            elif s==',':
                res.append(token)
                token=''
            else:
                token+=s
        i=i+1

    if len(token)>0:
        res.append(token)
    return res

            

def t(lines):
    res=[]
    for line in lines:
        res.append(parseT(line))

    return res

rst=t(csv_lines)
for v in rst:
    print v
"""
s='Jane,Roberts,janer@msn.com,"San Francisco, CA",0'
rst=parseT(s)
print rst
"""





