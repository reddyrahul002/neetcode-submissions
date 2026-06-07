# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0

        def diameter(root):
            if not root:
                return 0
            l_max=diameter(root.left)
            r_max=diameter(root.right)
            self.dia=max(self.dia,l_max+r_max)

            return 1+max(l_max,r_max)
        
        diameter(root)
        return self.dia
        