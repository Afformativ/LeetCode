class Solution:
    def coloredCells(self, n: int) -> int:
        colored_cells = 1
        for i in range(1, n+1):
            colored_cells += 4 * (i-1) + 1
        return colored_cells-n
