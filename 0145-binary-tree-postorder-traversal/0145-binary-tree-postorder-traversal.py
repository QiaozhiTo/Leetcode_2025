# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visit = [False]
        stack = [root]
        res = []
        while stack:
            v = visit.pop()
            curr = stack.pop()
            if curr: 
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return res
