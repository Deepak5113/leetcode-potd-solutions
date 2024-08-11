class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands():
            visited = [[False] * n for _ in range(m)]
            islands = 0
            
            def dfs(i, j):
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        visited[i][j] = True
                        dfs(i, j)
                        
            return islands

        m, n = len(grid), len(grid[0])

        # Initial check: If the grid is already disconnected
        if count_islands() != 1:
            return 0

        # Check after removing one land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1  # Revert the change

        # If we can't disconnect the grid by removing one cell, it takes 2 removals
        return 2