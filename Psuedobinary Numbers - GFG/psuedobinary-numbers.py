#User function Template for python3
class Solution:
	def minimumPseudoBinary(self, N):
		# code here
		k = []
        while N != 0:
            m = str(N)
            for i in m:
                if int(i) > 1:
                    m = m.replace(i,'1')
            k.append(int(m))
            N = N-int(m)
        return k
		            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.minimumPseudoBinary(N)
		for num in ans:
		    print(num,end=' ')
		print()
# } Driver Code Ends