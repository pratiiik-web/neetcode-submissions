class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        area = 0

        def dfs(r, c):
            if (r<0 or r == Rows or c<0 or c == Cols or grid[r][c] == 0 or (r, c) in visit):
                return 0    
            visit.add((r,c))
            return(1 + dfs(r+1, c)+
                       dfs(r-1, c)+
                       dfs(r, c+1)+
                       dfs(r, c-1))


        for r in range(Rows):
            for c in range(Cols):
                area = max(area, dfs(r, c))
        return area

