# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root == None:
                return
            left_tree = invert(root.left)
            right_tree = invert(root.right)
            root.left = right_tree
            root.right = left_tree
            return root
        return invert(root)
