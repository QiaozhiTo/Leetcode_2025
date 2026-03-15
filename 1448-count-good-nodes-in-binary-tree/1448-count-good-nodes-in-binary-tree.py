# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node: return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)
# dfs 内部的 return 是把值传给dfs的调用者，但 goodNodes 还需要再 return 一次才能把值传给goodNodes的调用者（也就是LeetCode的测试系统）。每个函数都只负责把值传给直接调用它的那一层。