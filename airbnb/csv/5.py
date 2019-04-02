
def t(s):
    res=[]
    i=0
    token=0
    while i<len(s):
        ch=s[i]
        if ch=='[':
            b=1
            j=i+1
            tmpS='['
            while j<len(s):
                if s[j]=='[':
                    b+=1
                if s[j]==']':
                    b-=1
                if b==0:
                    token=t(s[i+1:j])
                    print '24: ', s[i+1:j], i+1, j, token
                    if isinstance(token, list):
                        res.extend(token)
                    else:
                        res.append(token)
                    token=0
                    break
                j=j+1
            i=i+j
        elif ch.isdigit():
            token=token*10+int(ch)
        elif ch==',':
            res.append(token)
            token=0
        i=i+1
        print '34', res
    if token:
        res.append(token)
    print 'line30: ', res
    return res


#s='[123,456,[788,799,833],[[]],10,[]]'
s='[[12]]'
rst=t(s)
print rst


