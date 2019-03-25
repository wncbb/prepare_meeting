# -*- encoding: utf-8 -*-

class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    isMatch("aab", "c*a*b") → true
    """
    def isMatch(self, s, p):
        # write your code here
        dp=[False]*(len(p)+1)*(len(s)+1)
        print dp



s=Solution()
s='aab'
p='c*a*b'
print s.isMatch(s, p)
