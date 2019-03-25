class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        stack=[]
        num=0
        sign='+'
        
        for i in range(len(s)):
            ch=s[i]
            if ch.isspace():
                continue
            if ch.isdigit():
                num=num*10+int(ch)
            if (not ch.isdigit()) or i==len(s)-1:
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-1*num)
                elif sign=='*':
                    stack.append(stack.pop()*num)
                elif sign=='/':
                    stack.append(int(stack.pop())/float(num))
                num=0
                sign=ch


        return sum(stack)

s=Solution()
raw='12*13+14/14'
rst=s.calculate(raw)
print rst
