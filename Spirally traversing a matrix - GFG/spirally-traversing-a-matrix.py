#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        top,left=0,0
        right,bottom=c-1,r-1
        res=[]
        while left<=right and top<=bottom:
            
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
                
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
                
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
                    
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
                    
        return res
        
        '''
        row=0;col=0
        l=[]
        while row<r and col<c:
            for i in range(col,c):
                l.append(matrix[row][i])
            row+=1
            for j in range(row,r):
                l.append(matrix[j][c-1])
            c-=1
            
            if row<r:
                for i in range(col,c):
                    l.append(matrix[r-1][i])
                r=r-1
                
            if col<c:
                for j in range(row,r):
                    l.append(matrix[j][col])
                col+=1
        return l
        '''
            
        # code here 
'''

while row_start <= row_end and col_start <= col_end:
            for col in range(col_start, col_end + 1):
                ans.append(matrix[row_start][col])
        
            row_start += 1
            
            for row in range(row_start, row_end + 1):
                ans.append(matrix[row][col_end])
                
            col_end -= 1
            
            if row_start <= row_end:
                for col in range(col_end, col_start - 1, -1):
                    ans.append(matrix[row_end][col])
                
                row_end -= 1
            
            if col_start <= col_end:
                for row in range(row_end, row_start - 1, -1):
                    ans.append(matrix[row][col_start])
                
                col_start += 1
        
        return ans
        '''
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends