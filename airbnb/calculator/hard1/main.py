class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here   
        # Write your code here
        stack=[]
        result=0
        number=0
        sign=1
        for v in s:
            if v.isdigit():
                number=number*10+int(v)
            if v.isspace():
                continue

            if v=='+':
                result=result+sign*number
                number=0
                sign=1
            if v=='-':
                result=result+sign*number
                number=0
                sign=-1
            if v=='(':
                stack.append(result)
                stack.append(sign)
                sign=1
                result=0
            if v==')':
                result=result+sign*number
                number=0
                result*=stack.pop()
                result+=stack.pop()
        if number!=0:
            result+=sign*number
        return result


tmp="5+(1+2)-3"
s=Solution()
print s.calculate(tmp)
