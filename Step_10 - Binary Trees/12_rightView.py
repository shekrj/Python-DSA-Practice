class Solution:
    def rightSideView(self, root):
        res = []
        
        def dfs(node, level):
            if not node:
                return
            
            # first time visiting this level → record it
            if level == len(res):
                res.append(node.val)
            
            # right first ensures we capture rightmost node first
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return res
