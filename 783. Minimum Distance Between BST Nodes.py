# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if node:
                inorder(node.left)
                self.nodes.append(node.val)
                inorder(node.right)
                
        self.nodes = []
        inorder(root)
        
        min_diff = float('inf')
        for i in range(1, len(self.nodes)):
            diff = self.nodes[i] - self.nodes[i-1]
            if diff < min_diff:
                min_diff = diff
                
        return min_diff 
