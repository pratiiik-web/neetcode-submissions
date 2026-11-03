class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        raws, columns = len(grid), len(grid[0])

        def dfs(i, j):
            if grid[i][j] != '1':
                return 
            grid[i][j] = '0'
            if i>0:             #up
                dfs(i-1,j)
            if j<(columns-1):   #right
                dfs(i, j+1)
            if i<(raws-1):      #down
                dfs(i+1,j)
            if j>0:             #left
                dfs(i,j-1)

        count = 0    
        for i in range(raws):
            for k in range(columns):
                if grid[i][k] == '1':
                    dfs(i, k)
                    count+=1

        return count
