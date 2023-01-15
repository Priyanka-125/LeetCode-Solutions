
from collections import Counter
class Solution:
    def relativeSort (self,A1, N, A2, M):   
    
        dic={}
        for i in A1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=[]
        
        for i in A2:
            if i in dic.keys():
                ans.extend([i]*dic[i])
                del dic[i]
        final=[]
        for i in dic.keys():
            final.extend([i]*dic[i])
        final.sort()
        return ans + final

    

    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends