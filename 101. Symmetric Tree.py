# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q=deque([root])

        while q:
            level=[]
            for _ in range(len(q)):
                cur=q.popleft()
                level.append(cur.val if cur else '@')
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
            if len(level)>1:
                n=len(level)
                if level[:n//2]!=level[n//2:][::-1]:
                    return False
        return True

#Second Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(r1,r2):

            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            return r1.val==r2.val and helper(r1.left,r2.right) and helper(r1.right,r2.left)

        return helper(root,root)
