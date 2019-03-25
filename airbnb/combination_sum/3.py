class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        num=sorted(num)
        self.result=[]
        self.num=num
        self.target=target
        self.helper(target, [], 0)
        return self.result

    def helper(self, curTarget, curResult, curIndex):
        print 'curTarget:', curTarget, ', curResult:', curResult, ', curIndex:', curIndex
        if curTarget==0:
            self.result.append(curResult[:])
            return
        if curResult<0:
            return

        for i in range(curIndex, len(self.num)):
            if i>curIndex:
                if self.num[i]==self.num[i-1]:
                    continue
            curResult.append(self.num[i])
            # curIndex should be i+1, not i
            self.helper(curTarget-self.num[i], curResult, i+1)
            curResult.pop()




s=Solution()
num=[10,1,6,7,2,1,5]
target=8
rst=s.combinationSum2(num, target)
for v in rst:
    print v
