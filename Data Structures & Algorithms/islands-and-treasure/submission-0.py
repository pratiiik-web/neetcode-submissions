class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        Rows, Cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addgrid(r,c):
            if (r<0 or r == Rows or c<0 or c== Cols or grid[r][c] == -1 or (r, c) in visit):
                return
            visit.add((r,c))
            q.append([r, c])


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addgrid(r + 1, c)
                addgrid(r - 1, c)
                addgrid(r, c + 1)
                addgrid(r, c - 1)

            
            dist += 1