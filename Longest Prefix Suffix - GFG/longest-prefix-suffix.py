#User function Template for python3

class Solution:
	def lps(self, s):
		# code here
		n=len(s)
        k=0
        j=1
        while j+k<n:
            if s[k]==s[k+j]:
                k+=1
            else:
                j+=1
                k=0
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.lps(s)
		print(answer)

# } Driver Code Ends