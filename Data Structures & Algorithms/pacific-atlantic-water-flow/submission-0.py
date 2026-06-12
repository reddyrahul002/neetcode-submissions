class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r_len,c_len = len(heights),len(heights[0])
        pac=set()
        atl=set()
        result=[]
        def dfs(row,col,visited,prevh):
            if (row,col) in visited or row<0 or row>= r_len or col<0 or col>=c_len or heights[row][col]<prevh:
                return
            visited.add((row,col))
            dfs(row+1,col,visited,heights[row][col])
            dfs(row-1,col,visited,heights[row][col])
            dfs(row,col+1,visited,heights[row][col])
            dfs(row,col-1,visited,heights[row][col])
        for c in range(c_len):
            dfs(0,c,pac,heights[0][c])
            dfs(r_len-1,c,atl,heights[r_len-1][c])
        for r in range(r_len):
            dfs(r,0,pac,heights[r][0])
            dfs(r,c_len-1,atl,heights[r][c_len-1])
        for r in range(r_len):
            for c in range(c_len):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result
