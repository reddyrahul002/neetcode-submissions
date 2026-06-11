class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r_col,c_col=len(grid),len(grid[0])
        visited=set()
        count=0
        total = r_col*c_col
        maxi=0

        def dfs(row,col):
            if row<0 or col<0 or row>=r_col or col>=c_col:
                return 0
            if grid[row][col]!=1:
                return 0
            if (row,col) in visited:
                return 0

            visited.add((row,col))

            return 1+dfs(row+1,col)+dfs(row-1,col)+dfs(row,col+1)+dfs(row,col-1)

            
        for i in range(total):
            row=i//c_col
            col=i%c_col
            count=0
            if grid[row][col]==1 and (row,col) not in visited:
                maxi=max(maxi,dfs(row,col))
        return maxi   
                


                