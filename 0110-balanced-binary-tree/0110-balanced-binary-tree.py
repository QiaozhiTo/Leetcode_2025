# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def dfs(root):
#             if not root:return [True,0]
#             left = dfs(root.left)
#             right = dfs(root.right)
#             isBalanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
#             return [isBalanced, 1 + max(left[1], right[1])]
#         return dfs(root)[0]
        
         
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diff = abs(leftHeight - rightHeight)
        return diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def maxHeight(self, root):
        if not root:return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))