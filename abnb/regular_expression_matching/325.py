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
        dp=[[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        print dp

        dp[0][0]=True
        for i in range(1, len(p)):
            if p[i]=='*' or p[i]=='?':
                dp[0][i+1]=dp[0][i-1]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j]=='.':
                    dp[i+1][j+1]=dp[i][j]
                elif p[j]=='*':
                    if p[j-1]==s[i] or p[j-1]=='.':
                        dp[i+1][j+1]=dp[i][j+1] or dp[i][j-1]
                    dp[i+1][j+1]=dp[i+1][j+1] or dp[i+1][j-1]
                elif p[j]=='+':
                    if p[j-1]==s[i] or p[j-1]=='.':
                        dp[i+1][j+1]=dp[i][j+1] or dp[i][j-1]
                elif p[j]=='?':
                    if p[j-1]==s[i] or p[j-1]=='.':
                        dp[i+1][j+1]=dp[i][j]
                    dp[i+1][j+1]=dp[i+1][j+1] or dp[i+1][j-1]
                else:
                    if s[i]==p[j]:
                        dp[i+1][j+1]=dp[i][j]


        return dp[len(s)][len(p)]




c=Solution()
s='aabb'
p='a?bb'
print c.isMatch(s, p)
