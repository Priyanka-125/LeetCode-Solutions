#User function Template for python3

class Solution:
    def rremove (self, s):
		#code here
		if len(s)<=1:
		    return s
		n=len(s)
		ans=''
		i=0
		while i<n:
		    if i<n-1 and s[i]==s[i+1]:
		        while i<n-1 and s[i]==s[i+1]:
		            i+=1
		    else:
		        ans+=s[i]
		    i+=1
		
		if ans==s:
		    return s
		
	    return self.rremove(ans)
		        
		    
		    
'''		    
if len(S)<=1:
            return S
        
        i=0
        n=len(S)
        ans=''
        while(i<n):
            if(i<n-1 and S[i]==S[i+1]):
                while(i<n-1 and S[i]==S[i+1]):
                    i+=1
            else:
                ans=ans+S[i]
            i+=1
        #print(ans)
        if ans==S:
            return ans
        else:
            return(self.rremove(ans))
'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends