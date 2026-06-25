# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        qu = []
        qu.append(root)

        while len(qu) != 0:
            node = qu.pop(0)
            if node:
                node.left,node.right = node.right,node.left 
                qu.append(node.left)
                qu.append(node.right)

        return root
