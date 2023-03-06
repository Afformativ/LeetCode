# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        def traverse(node, level):
            if node is None:
                return
            if level >= len(level_sums):
                level_sums.append(node.val)
            else:
                level_sums[level] += node.val
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        traverse(root, 0)
        largest_sums = []
        for sum in level_sums:
            heapq.heappush(largest_sums, sum)
            if len(largest_sums) > k:
                heapq.heappop(largest_sums)
        if len(largest_sums) < k:
            return -1
        return largest_sums[0]
        
