# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count pairs
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1
            
            # Collect all distances for this node
            current_distances = []
            for l in left_distances:
                if l + 1 <= distance:
                    current_distances.append(l + 1)
            for r in right_distances:
                if r + 1 <= distance:
                    current_distances.append(r + 1)
            
            return current_distances
        
        self.result = 0
        dfs(root)
        return self.result