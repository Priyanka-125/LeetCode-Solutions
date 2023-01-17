#User function Template for python3
class Solution:
	def setKthBit(self, n, k):
		# code here
		n=bin(n)
		n=n.split("b")[1]
		n=n[::-1]
		n=list(str(n))
		if n[k]=='0':
		    n[k]="1"
		n=n[::-1]
		#print(n)
		ans=""
		for i in n:
		    ans=ans+i
		return int(ans,2)
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,K = input().split()
		N = int(N)
		K = int(K)
		ob = Solution()
		ans = ob.setKthBit(N,K)
		print(ans)




# } Driver Code Ends