class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_row_elements = [max(grid[i]) for i in range(rows)]
        max_col_elements = [max(grid[j][i] for j in range(rows)) for i in range(cols)]
        for i in range(len(max_row_elements)):
            for j in range(len(max_col_elements)):
                grid[i][j]=abs(grid[i][j]-min(max_row_elements[i],max_col_elements[j]))
        res=0
        for i in range(len(grid)):
            res+=sum(grid[i])
        return res
