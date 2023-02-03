#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        x=n*(n+1)//2
        s=sum(arr)
        arr.sort()
        for i in range(n):
            if arr[i]==arr[i+1]:
                l=arr[i]
                break
        a=x-(s-l)
        return l,a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends