#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        if len(arr)<4:
            return -1
        
        arr.sort()
        sett=set()
        n=len(arr)
        left=0
        right=0
        sum=0
        for i in range(0,n-3):
            for j in range(i+1,n-2):
                left=j+1
                right=n-1
                while left<right:
                    sum=arr[i]+arr[j]+arr[left]+arr[right]
                    if sum>k:
                        right-=1
                    elif sum==k:
                        temp=(arr[i],arr[j],arr[left],arr[right])
                        sett.add(temp)
                        left+=1
                    else:
                        left+=1
                        
        return sorted(list(sett))
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends