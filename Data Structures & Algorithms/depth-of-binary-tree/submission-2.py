# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def max_path(root):
    if not root:
        return 0
    l_max = max_path(root.left)             
    r_max = max_path(root.right)             
    return 1 + max(l_max, r_max)  


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_path(root)

        