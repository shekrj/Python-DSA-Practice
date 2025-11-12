from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left=left
        self.right=right
        self.val=val
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth=self.maxDepth(root.left)
        rightDepth=self.maxDepth(root.right)
        return 1+max(leftDepth, rightDepth)