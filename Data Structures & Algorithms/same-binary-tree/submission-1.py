# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []

        def dfs(node, arr):
            if not node:
                arr.append(None)
                return
            dfs(node.left, arr)
            dfs(node.right, arr)
            arr.append(node.val)
        dfs(p, res1)
        dfs(q, res2)
        return res1 == res2

