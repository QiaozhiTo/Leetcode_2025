# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.height(root.left)
        right = self.height(root.right)
        diameter = left + right
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(sub, diameter)

    def height(self, root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))

# dfs
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            # return 1 + max(dfs(node.left), dfs(node.right))
            return 1 + max(left, right)
        dfs(root)
        return res
            