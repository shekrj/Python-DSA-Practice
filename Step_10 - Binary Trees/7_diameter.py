# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0  # global variable to store max diameter

        def dfs(node):
            if not node:
                return 0  # height = 0 for null node
            
            left = dfs(node.left)
            right = dfs(node.right)

            # update global diameter if longer path found
            self.diameter = max(self.diameter, left + right)

            # return height for this node
            return 1 + max(left, right)

        dfs(root)
        return self.diameter
