from collections import deque

def t(s):
    i=0
    stack=[]
    token=None
    res=[]
    while i<len(s):
        ch=s[i]
        if ch=='[':
            stack.append(ch)
        elif ch==']':
            tmpList=[]
            while stack[-1]!='[':
                stackItem=stack.pop()
                if stackItem is not None:
                    tmpList.append(stackItem)
            stack.pop()
            tmpList.reverse()
            stack.append(tmpList)
        elif ch==',':
            stack.append(token)
            token=None
        elif ch.isdigit():
            if len(stack)==0:
                stack.append(int(ch))
            elif isinstance(stack[-1], int):
                stack.append(stack.pop()*10+int(ch))
            else:
                stack.append(int(ch))
        i=i+1

    return stack[0]

#s='[123,456,[[788,799,833]],[[]],10,[]]'
s='[12,14]'
rst=t(s)
print rst
