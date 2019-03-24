class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        sorted_num = sorted(num)
        res = []
        self.dfs(sorted_num, 0, [], res, target)
        return res
        
    def dfs(self, A, idx, buf, res, target):
        if target == 0:
            res.append(buf)
            return
        
        if idx == len(A):
            return
        
        if target < 0 and A[idx] >= 0:
            return
        
        for k in xrange(idx, len(A)):
            if k > idx and A[k] == A[k-1]:
                continue
            self.dfs(A, k+1, buf + [A[k]], res, target - A[k])
