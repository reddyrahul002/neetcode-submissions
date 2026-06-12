class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r_len,c_len=len(board),len(board[0])
        visited=set()
        count=0

        def dfs(row,col):
            if row<0 or col<0 or row==r_len or col ==c_len or board[row][col]!='O':
                return
            board[row][col]="T"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
            

        for r in range(r_len):
            for c in range(c_len):
                if (board[r][c]=="O" and (r in [0,r_len-1] or c in [0,c_len-1])):
                    dfs(r,c)
        for r in range(r_len):
            for c in range(c_len):
                if board[r][c]=="O":
                    board[r][c]='X'

        for r in range(r_len):
            for c in range(c_len):
                if board[r][c]=="T":
                    board[r][c]='O'


        






        