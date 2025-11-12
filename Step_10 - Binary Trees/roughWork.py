from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
        
   
    def levelTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res=[]
        q=deque([root])
        while q:
            level=[]
            for _ in range(len(q)):
                temp=q.popleft()
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            res.append(level)
        return res
    

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth=self.maxDepth(root.left)
        rightDepth=self.maxDepth(root.right)
        return 1+max(leftDepth, rightDepth)
    

    def balancedBT(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            leftDepth=self.balancedBT(node.left)
            if leftDepth==-1:
                return -1
            
            rightDepth=self.balancedBT(node.right)
            if rightDepth==-1:
                return -1
            
            if abs(leftDepth-rightDepth)>1:
                return -1
            return 1+max(leftDepth, rightDepth)
        
        return dfs(root)
    
    def diameter(self, root: TreeNode) -> int:
        self.maxi=0
        def dfs(node):
            if not node:
                return 0
            leftDepth=dfs(node.left)           
            rightDepth=dfs(node.right)
            self.maxi=max(self.maxi, leftDepth+rightDepth)
            return 1+max(leftDepth, rightDepth)
        dfs(root)
        return self.maxi

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxi=float('-inf')
        def dfs(node):
            if not node:
                return 0
            leftSum=max(dfs(node.left), 0)
            rightSum=max(dfs(node.right), 0)
            currentSum=node.val+leftSum+rightSum
            self.maxi=max(self.maxi, currentSum)
            return node.val+max(leftSum, rightSum)
        dfs(root)
        return self.maxi
    
    def sameTree(self, r1: TreeNode, r2: TreeNode) -> bool:
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.val!=r2.val:
            return False
        res1=self.sameTree(r1.left, r2.left)
        res2=self.sameTree(r1.right, r2.right)
        if res1 and res2:
            return True
        return False
    
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
    
    def rightView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        q=deque([root])
        while q:
            level_size=len(q)
            for i in range(level_size):
                temp=q.popleft()
                if i==level_size-1:
                    res.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return res
    
    def leftView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        q=deque([root])
        while q:
            level_size=len(q)
            for i in range(level_size):
                temp=q.popleft()
                if i==0:
                    res.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return res
    
    def rootToNode(self, root: TreeNode, target: TreeNode) -> List[int]:
        st=[]
        def dfs(node):
            if not node:
                return False
            
            st.append(node.val)
            if node.val==target:
                return True
            
            if dfs(node.left) or dfs(node.right):
                return True
            
            st.pop()
            return False
        
        dfs(root)
        return st
    

    def rootToNode(self, root: TreeNode, target: TreeNode) -> List[int]:
        st=[]
        def dfs(node):
            if not node:
                return
            st.append(node.val)
            if node.val==target:
                return True

            if dfs(node.left) or dfs(node.right):
                return True
            st.pop()
            return False
        return st
    
    def lca(self, root: TreeNode, n1:TreeNode, n2: TreeNode) -> int:
        def dfs(node):
            if not node:
                return None
            if node==n1 or node==n2:
                return node
            left=dfs(node.left)
            right=dfs(node.right)
            if left and right:
                return node
            if left:
                return left
            return right
        return dfs(root)