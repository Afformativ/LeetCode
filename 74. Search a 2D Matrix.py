#solution 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag=False
        for i in matrix:
            for j in i:
                if j==target:
                    flag=True
        return flag

#solution 2
if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
