class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addGrid(r, c):
            if (r<0 or r == Rows or c<0 or c == Cols or (r, c) in visit or grid[r][c]==-1):
                return
            visit.add((r,c))
            q.append([r,c])


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                addGrid(r+1, c)
                addGrid(r-1, c)
                addGrid(r, c+1)
                addGrid(r, c-1)
                

            dist += 1