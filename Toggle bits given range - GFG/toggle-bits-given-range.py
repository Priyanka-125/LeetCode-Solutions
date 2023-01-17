#User function Template for python3

class Solution:
    def toggleBits(self, n , L , R):
        # code here 
        n=bin(n)
        n=n.split("b")[1]
        n=list(str(n))
        
        for i in range(L,R+1):
            if n[-i]=="0":
                n[-i]="1"
            else:
                n[-i]="0"
        ans=""
        for i in range(len(n)):
            ans+=n[i]
            
        return int(ans,2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.toggleBits(N,L,R))
# } Driver Code Ends