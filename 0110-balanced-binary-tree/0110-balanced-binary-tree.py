# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        if abs(left_depth-right_depth) > 1:
            self.ans = False
        return max(left_depth,right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDepth(root)
        return self.ans