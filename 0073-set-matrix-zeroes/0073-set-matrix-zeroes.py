class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        a=[]
        b=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    a.append(i)
                    b.append(j)
        for i in a:
            for j in range(n):
                matrix[i][j]=0
        for i in b:
            for j in range(m):
                matrix[j][i]=0
        