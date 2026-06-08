# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def check_balance(self,root):
    if not root:
       return 0
    l_max=check_balance(self,root.left)
    r_max=check_balance(self,root.right)
    if abs(r_max-l_max)>1:
        self.isbalanced=False
    return 1+max(l_max,r_max)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced=True

        height = check_balance(self,root)

        return self.isbalanced
           
        