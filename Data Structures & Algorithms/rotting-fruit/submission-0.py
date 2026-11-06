class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        time, fresh = 0, 0

        Rows, Cols = len(grid), len(grid[0])
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rows, cols = dr + r, dc + c
                    # if in bound, and fresh make rotten
                    if (rows < 0 or rows == Rows or cols < 0 or cols == Cols or grid[rows][cols] != 1):
                        continue
                    
                    grid[rows][cols] = 2
                    q.append([rows, cols])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1