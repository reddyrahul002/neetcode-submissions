class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
   
        i,k=0,len(matrix)-1
        row=0
        while i<=k :
            mid_row= (i+k)//2
            if  target <= matrix[mid_row][-1] and  target >= matrix[mid_row][0]:
                row=mid_row
                break 
            elif target < matrix[mid_row][0]:
                k=mid_row-1
            elif target > matrix[mid_row][-1]:
                i=mid_row+1
            else :
                return False
        
        l,r=0,len(matrix[row])-1
        while l<=r :
            mid_col= (l+r)//2
            if matrix[row][mid_col] == target:
                return True 
            elif target < matrix[row][mid_col]:
                r=mid_col-1
            elif target > matrix[row][mid_col]:
                l=mid_col+1
            else :
                return False
        return False
            


    




