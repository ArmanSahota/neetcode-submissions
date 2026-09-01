# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        def isLeaf(node):
            return not node.left and not node.right
        
        def leftB(node):
            cur = node
            while cur:
                if not isLeaf(cur):
                    res.append(cur.val)
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right
        def rightB(node):
            cur = node
            stack = []
            while cur:
                if not isLeaf(cur):
                    stack.append(cur.val)
                if cur.right:
                    cur = cur.right
                else:
                    cur = cur.left
            while stack:
                res.append(stack.pop())
        def leaves(node):
            if not node:
                return
            if isLeaf(node):
                res.append(node.val)
            leaves(node.left)
            leaves(node.right)


        if not isLeaf(root):
            res.append(root.val)    
        leftB(root.left)
        leaves(root)
        rightB(root.right)

        return res








