#User function Template for python3

class Solution:
    def median(self, matrix, R, C):
    	#code here 
    	l=[];mid=0
    	for i in matrix:
    	    for j in i:
    	        l.append(j)
    	l.sort()
    	mid=len(l)//2
    	return l[mid]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends