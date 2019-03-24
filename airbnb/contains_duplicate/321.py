# -*- encoding: utf-8 -*-
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @param t: the given t
    @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
    """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Write your code here
        if len(nums)<=1:
            return False
        bucketWidth=t+1
        lookup={}
        minNum=nums[0]
        for i in range(1, len(nums)):
            if nums[i]<minNum:
                minNum=nums[i]

        bktWidth=t+1
        for idx in range(len(nums)):
            i=nums[idx]
            realNum=i-minNum
            bktIdx=realNum/bktWidth
            if bktIdx in lookup:
                # print '26, bktIdx:', bktIdx, ' idx:', idx, ' i:', i, 'lookup:', lookup
                return True
            leftIdx=bktIdx-1
            if leftIdx in lookup:
                if abs(lookup[leftIdx]-realNum)<=t:
                    # print '31'
                    return True
            rightIdx=bktIdx+1
            if rightIdx in lookup:
                if abs(lookup[rightIdx]-realNum)<=t:
                    # print '36'
                    return True
            # should be >=, not >
            if len(lookup)>=k:
                # 这里要用realNUm
                del lookup[((nums[idx-k]-minNum)/bktWidth)]

            # print '42 bktIdx:', bktIdx, ' realNum:', realNum, 'lookup:', lookup
            lookup[bktIdx]=realNum
            # print '44 bktIdx:', bktIdx, ' realNum:', realNum, 'lookup:', lookup
        return False

nums = [1,3,1]
k = 1 
t = 1
s=Solution()
print s.containsNearbyAlmostDuplicate(nums, k, t)
