# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')  # global variable to track max sum

        def dfs(node):
            if not node:
                return 0

            # max gain from left and right (ignore negative paths)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # price of the path going through this node
            current_path_sum = node.val + left_gain + right_gain

            # update global max
            self.max_sum = max(self.max_sum, current_path_sum)

            # return max gain to continue path upward
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
