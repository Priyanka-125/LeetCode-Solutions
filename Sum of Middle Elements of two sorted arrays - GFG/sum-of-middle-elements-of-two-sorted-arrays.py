#User function Template for python3

class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here 
		for i in range(n):
		    ar1.append(ar2.pop())
		ar1.sort()
		mid=(n*2)//2
		sum=ar1[mid-1]+ar1[mid]
		return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends