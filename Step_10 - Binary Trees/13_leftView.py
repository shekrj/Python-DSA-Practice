class Solution:
    def leftSideView(self, root):
        res = []

        def dfs(node, level):
            if not node:
                return
            
            # if first node at this level → visible from left
            if level == len(res):
                res.append(node.val)
            
            # go left first, then right
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return res
