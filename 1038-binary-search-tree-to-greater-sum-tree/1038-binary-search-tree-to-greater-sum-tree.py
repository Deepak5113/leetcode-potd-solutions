# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.reverse_inorder(root)
        return root
    
    def reverse_inorder(self, node):
        if not node:
            return
        
        # Traverse the right subtree first
        self.reverse_inorder(node.right)
        
        # Update the node's value with the sum of greater nodes
        self.sum += node.val
        node.val = self.sum
        
        # Traverse the left subtree
        self.reverse_inorder(node.left)