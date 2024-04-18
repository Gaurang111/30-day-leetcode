# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        self.result = ""
        self.search(root, "")
        return self.result

    def search(self, node, path):
        if not node:
            return

        path = chr(node.val + ord('a')) + path

        if not node.left and not node.right:
            if not self.result or self.result > path:
                self.result = path

        self.search(node.left, path)
        self.search(node.right, path)
