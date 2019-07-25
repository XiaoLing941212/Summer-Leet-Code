'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
'''

#DFS:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        ans = 0
        visited = set()
        
        def dfs(row, col):
            visited.add((row, col))
            around = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            
            for r, c in around:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
        
        return ans
