# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        # both are null
        if not p and not q:
            return True
        
        # one is null, other is not
        if not p or not q:
            return False
        
        # values differ
        if p.val != q.val:
            return False

        # check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
