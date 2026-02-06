# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Brute
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        left = self.height(root.left)
        right = self.height(root.right)
        return (abs(left - right) <= 1 and 
                self.isBalanced(root.left) and 
                self.isBalanced(root.right))

    def height(self, root):
        if not root:return 0
        return 1 + max(self.height(root.left), self.height(root.right))
        

# dfs
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

        