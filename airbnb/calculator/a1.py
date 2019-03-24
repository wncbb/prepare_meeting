
class Solution:
    def calculate(self, s):
        num=0
        op='+'
        stack=[]
        s=s.strip()
        for i in range(len(s)):
            ch=s[i]
            if ch.isdigit():
                num=num*10 + int(ch)
            elif ch.isspace():
                continue
            if (not ch.isdigit()) or i==(len(s)-1):
                if op=='+':
                    stack.append(num)
                elif op=='-':
                    stack.append(-num)
                elif op=='*':
                    stack.append(stack.pop()*num)
                elif op=='/':
                    stack.append(int(stack.pop()/float(num)))
                num=0
                op=ch
        return sum(stack)


s=Solution()
print s.calculate("13*3-1")
