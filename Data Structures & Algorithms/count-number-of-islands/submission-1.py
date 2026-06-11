class Solution:
    
    
    
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        c_len=len(grid[0])
        r_len=len(grid)
        total = r_len*c_len
        visited=set()
        count=0

        def dfs(row,col):
            if row <0 or row >= r_len or col <0 or col >= c_len:
                return 
            if grid[row][col] !='1':
                return
            if (row,col) in visited:
                return
            visited.add((row,col))
            dfs(row+1,col) 
            dfs(row-1,col)
            dfs(row,col+1) 
            dfs(row,col-1) 

        for i in range(total):
            row=i//c_len
            col=i%c_len
            if grid[row][col]=='1' and (row, col) not in visited :
                count+=1
                dfs(row,col)
        return count

        


        