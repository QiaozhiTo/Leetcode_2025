# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# brute force
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        diameter = left + right
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(sub, diameter)
    def maxHeight(self, root):
        if not root: return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

# dfs
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.res = 0
#         def dfs(node):
#             if not node: return 0
#             left = dfs(node.left)
#             right = dfs(node.right)
#             self.res = max(self.res, left + right)
#             return 1 + max(left, right)
#         dfs(root)
#         return self.res
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # a global res
        self.res = 0
        # return height
        def dfs(curr):
            if not curr:return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right) #height of node curr
        dfs(root)
        return self.res

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #local res
        res = 0
        # return height
        def dfs(curr):
            if not curr:return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right) #height of a node
        dfs(root)
        return res

'''        