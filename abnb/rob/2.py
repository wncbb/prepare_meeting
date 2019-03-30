class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
        
        
    def rob1(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        prev = 0
        crt = nums[0]
        for num in nums[1:]:
            prev, crt = crt, max(prev + num, crt)
            
        return crt