# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        ls=[]
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            ls.append(root.val)
            dfs(root.right)
            
            return root.val
        
        x=dfs(root)
        return ls[k-1]