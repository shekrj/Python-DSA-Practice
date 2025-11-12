class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getPath(root, target):
    path = []

    def dfs(node):
        if not node:
            return False

        # include current node in path
        path.append(node.data)

        # if target found
        if node.data == target:
            return True

        # search in left or right subtree
        if dfs(node.left) or dfs(node.right):
            return True

        # backtrack
        path.pop()
        return False

    dfs(root)
    return path
