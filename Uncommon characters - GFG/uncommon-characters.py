#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        s="";p=""
        for i in A:
            if i not in B:
                s=s+i
        for i in B:
            if i not in A:
                s=s+i
        l=[i for i in s]
        l=list(set(l))
        l.sort()
        for i in l:
            p=p+i
        if p:
            return p
        else:
            return "-1"
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends