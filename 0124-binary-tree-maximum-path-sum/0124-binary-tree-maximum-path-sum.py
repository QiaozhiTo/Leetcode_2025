# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node: return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            # with spliting
            res[0] = max(res[0], leftMax + rightMax + node.val)
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]

