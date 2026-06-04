class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={}
        column={}
        box={}
        for i in range(0,9):
            for j in range(0,9):
                
                value = board[i][j]

                if value == '.':
                    continue
                
                index= (i//3,j//3)

                if i not in row : row[i]=[]
                if j not in column : column[j]=[]
                if index not in box : box[index]=[]

                if value in row[i] or value in column[j] or value in box[index] :
                    return False
                
                row[i].append(value)
                column[j].append(value)
                box[index].append(value)
                
        return True
        
                
        
        



                

        

            
        

                

