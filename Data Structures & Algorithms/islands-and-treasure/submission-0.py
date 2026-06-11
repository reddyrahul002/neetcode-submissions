class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r_len,c_len=len(grid),len(grid[0])
        total = r_len * c_len
        queue = deque()
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(total):
            r=i//c_len
            c=i%c_len
            if grid[r][c] == 0:
                queue.append((r, c))
                visited.add((r, c))
        dist = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col]=dist
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if 0<=nr<r_len and 0<=nc<c_len and (nr,nc) not in visited and grid[nr][nc] != -1:
                        visited.add((nr,nc))
                        queue.append((nr, nc))
                        
            dist += 1



            


        