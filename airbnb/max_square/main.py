class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        
        for i in range(n): 
            dp[0][i] = matrix[0][i]
        for i in range(1, m): 
            dp[i][0] = matrix[i][0]

        for i in xrange(1, m):
            for j in xrange(1, n): 
                if not matrix[i][j]: 
                    dp[i][j] = 0
                else: 
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans=max(ans, dp[i][j])
        
        return ans ** 2
