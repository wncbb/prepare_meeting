"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        robVal, skipVal=self.helper(root)
        return max(robVal, skipVal)
    
    def helper(self, node):
        if not node:
            return 0
        
        leftRob, leftSkip=self.helper(node.left)
        rightRob, rightSkip=self.helper(node.right)
        rob=node.val+leftSkip+rightSkip
        skip=max(leftRob, leftSkip)+max(rightRob, rightSkip)
        return rob, skip