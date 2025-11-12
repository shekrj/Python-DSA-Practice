# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)
        
        return isMirror(root.left, root.right)
    

    def symmetricTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        def dfs(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val!=r2.val:
                return False
            res1=dfs(r1.left, r2.right)
            res2=dfs(r1.right, r2.left)
            if res1 and res2:
                return True
            return False
        res=dfs(root.left, root.right)
        return res