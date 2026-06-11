class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        r_len=len(board)
        c_len=len(board[0])
        total=r_len*c_len
        visited=set()
        def dfs(row,col,index):
                if index==len(word):
                    return True
                if row < 0 or row >= r_len or col < 0 or col >= c_len:
                    return False
                if board[row][col]!=word[index]:
                    return False
                if (row, col) in visited:                       
                    return False
                visited.add((row, col))
                found = (dfs(row+1,col,index+1) or dfs(row-1,col,index+1) or
                        dfs(row,col+1,index+1) or dfs(row,col-1,index+1))
                visited.remove((row, col))
                return found
        for i in range(total):
            row, col = i//c_len, i%c_len
            if dfs(row, col, 0):       
                return True
        return False

