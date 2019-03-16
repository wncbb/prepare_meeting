class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'

        s = s.strip()
        for i, c in enumerate(s):
            print 'num:', num, ' op:', op, ' c:', c, ' i:', i
            if c == ' ': continue
            elif '0' <= c and c <= '9':
                num = num * 10 + int(c)
            if c < '0' or c > '9' or i == len(s)-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                else:
                    if op == '*': stack.append(stack.pop() * num)
                    if op == '/': stack.append(int(stack.pop()/float(num)))
                op = c
                num = 0

        return sum(stack)
s=Solution()
raw='12*13+14'
rst=s.calculate(raw)
print rst
