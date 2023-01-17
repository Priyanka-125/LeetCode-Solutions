#User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        if len(S) == 1:
            return S
        else:
            sorted_s = sorted(list(S))
            #print(sorted_s)
            result = []
            for i in range(len(S)):
                for j in self.find_permutation(sorted_s[:i]+sorted_s[i+1:]):
                    permutation = sorted_s[i]+j
                    #print(permutation)
                    if permutation not in result:
                        result.append(permutation) 
            return result
        
        '''
        import itertools
        def fun(s):
            ans=[]
            permutations=itertools.permutations(s,len(s))
            for word in permutations:
                ans.append("".join(word))
            for i in sorted(ans):
                print(i)
                
        '''
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends