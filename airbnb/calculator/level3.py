class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        opStack = []
        numStack = []
        s = '(' + s + ')'
        cur_num = 0
        for i, c in enumerate(s):
            if c == ' ':
                continue
            if ord('0') <= ord(c) <= ord('9'):
                cur_num = cur_num * 10 + (ord(c) - ord('0'))
            elif c == '(':
                opStack.append('(')
                opStack.append('+')
            else:
                if opStack[-1] == '/':
                    cur_num = numStack.pop() // cur_num
                    opStack.pop()
                elif opStack[-1] == '*':
                    cur_num = numStack.pop() * cur_num
                    opStack.pop()
                if c == ')':
                    if opStack[-1] == '-':
                        cur_num = -cur_num
                    opStack.pop()
                    while opStack[-1] != '(':
                        if opStack[-1] == '-':
                            cur_num += -numStack.pop()
                        else:
                            cur_num += numStack.pop()
                        opStack.pop()
                    opStack.pop()
                else:
                    opStack.append(c)
                    numStack.append(cur_num)
                    cur_num = 0
        return cur_num
