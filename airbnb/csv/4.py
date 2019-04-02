# -*- encoding: utf8 -*-


s='aa,bb,"aa","aa,bb","aa""aa"""'

def parseStr(s):
        res=[]
        isQuote=False
        i=0
        token=''
        while i<len(s):
                if isQuote:
                        if s[i]=='"':
                                if i<len(s)-1 and s[i+1]=='"':
                                        token+='"'
                                        i=i+1
                                elif i<len(s)-1 and s[i+1]==',':
                                        isQuote=False
                                        i=i+1
                                        res.append(token)
                                        token=''
                                else:
                                        token+=s[i]

                else:
                        if s[i]==',':
                                res.append(token)
                                token=''
                        elif s[i]=='"':
                                isQuote=True
                        else:
                                token+=s[i]

                i=i+1
                print token
        print res
        return '|'.join(res)

s='aa,bb,"aa","aa,bb","aa""aa"""'
rst=parseStr(s)
print rst
