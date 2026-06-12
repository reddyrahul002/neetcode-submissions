class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r_len,c_len=len(grid),len(grid[0])
        total=r_len*c_len
        visited=set()
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(total):
            row=i//c_len
            col=i%c_len
            if grid[row][col]==2:
                queue.append((row,col))
                visited.add((row,col))
        minutes=-1
        while queue:
            minutes+=1
            for i in range(len(queue)):
                row,col=queue.popleft()
                grid[row][col]=2
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if 0<=nr<r_len and 0<=nc<c_len and (nr,nc) not in visited and grid[nr][nc]==1:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        for r in range(r_len):
            for c in range(c_len):
                if grid[r][c] == 1:
                    return -1
        return max(minutes, 0)


            


        

        