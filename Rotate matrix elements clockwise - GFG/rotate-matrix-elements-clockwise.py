#User function Template for python3

class Solution:
    def rotateMatrix(self, m, n, mat):
        #code here
        row = col = 0
       
        while row < m and col < n:
            
            if row + 1 == m or col + 1 == n: 
                break
       
            prev = mat[row + 1][col]
           
            for i in range(col, n):
                mat[row][i], prev = prev, mat[row][i]
            
            row += 1
            
            for j in range(row, m):
                mat[j][n - 1], prev = prev, mat[j][n - 1]
            n -= 1
               
            if row < m:
                for i in range(n - 1, col - 1, -1):
                    mat[m - 1][i], prev = prev, mat[m - 1][i]
            m -= 1
           
            if col < n:
                for j in range(m - 1, row - 1, -1):
                    mat[j][col], prev = prev, mat[j][col]
            col += 1
           
        return mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        ans=ob.rotateMatrix(N,M,A)
        for i in range(N):
            for j in range(M):
                print(ans[i][j],end=" ")
            print()    
# } Driver Code Ends