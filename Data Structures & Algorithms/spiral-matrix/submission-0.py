class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,top=0,0
        r,bottom=len(matrix[0])-1,len(matrix)-1
        result=[]
        while l<=r and top<=bottom:
        
            for i in range(l,r+1):
                result.append(matrix[top][i])
            for j in range(top+1,bottom+1):
                result.append(matrix[j][r])
            for k in range(r-1,l-1,-1):
                if top < bottom:
                    result.append(matrix[bottom][k])
            for m in range(bottom-1,top,-1):
                if l<r:
                    result.append(matrix[m][l])
            l+=1
            r-=1
            top+=1
            bottom-=1
        return result

            