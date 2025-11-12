from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def zigzagTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res=[]
        q=deque([root])
        flag=False
        while q:
            level=[]
            for _ in range(len(q)):
                temp=q.popleft()
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            if flag:
                level.reverse()

            res.append(level)
            flag=not flag
        return res   