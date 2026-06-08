# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isequal(root,subRoot):  
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return isequal(root.left,subRoot.left) and isequal(root.right,subRoot.right) 
        def checkSubtree(root,subRoot) :
            if not root:
                return False
            if isequal(root,subRoot):
                return True
            return checkSubtree(root.left,subRoot) or checkSubtree(root.right,subRoot)
        return checkSubtree(root,subRoot)

        