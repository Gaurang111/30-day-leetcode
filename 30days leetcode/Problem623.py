# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insert_node(self, root, val, target_depth, current_depth):
        if not root:
            return None

        if current_depth == target_depth - 1:
            left_subtree = root.left
            right_subtree = root.right

            root.left = TreeNode(val)
            root.right = TreeNode(val)
            root.left.left = left_subtree
            root.right.right = right_subtree

            return root

        root.left = self.insert_node(root.left, val, target_depth, current_depth + 1)
        root.right = self.insert_node(root.right, val, target_depth, current_depth + 1)

        return root

    def addOneRow(self, root, val, depth):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        return self.insert_node(root, val, depth, 1)
