
#dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid),len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self._dfs(grid,i,j)
        return count


    def _dfs(self, grid, r, c):
        grid[r][c]='0'
        for  x,y in ((r-1, c),(r+1,c),(r,c-1),(r,c+1)):
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1':
                self._dfs(grid, x, y)
