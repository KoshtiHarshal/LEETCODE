# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.Max = float('-inf')
        self.solve(root)
        return self.Max

    def solve(self, node):
        if not node:
            return 0
        
        left_sum = max(0, self.solve(node.left))
        right_sum = max(0, self.solve(node.right))
        
        self.Max = max(self.Max, node.val + left_sum + right_sum)
        
        return node.val + max(left_sum, right_sum)