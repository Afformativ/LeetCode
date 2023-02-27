# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        Q=deque([root])
        while Q:
            runsum=0
            for i in range(len(Q)):
                node=Q.popleft()
                runsum+=node.val
                if node.right:
                    Q.append(node.right)
                if node.left:
                    Q.append(node.left)
        return runsum

        
