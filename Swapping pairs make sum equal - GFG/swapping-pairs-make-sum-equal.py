class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum1=sum(a)
        sum2=sum(b)
        target=0;i=0;j=0;diff=0
        '''
        newsum1=0
        newsum2=0
        for i in range(n):
            for j in range(m):
                newsum1=sum1-i+j
                newsum2=sum2-j+i
                if newsum1==newsum2:
                    return 1
        return -1
        '''
        a.sort()
        b.sort()
        if( (sum1-sum2)%2!=0):
            target=-float('inf')
        else:
            target=(sum1-sum2)//2
        while i<n and j<m:
            diff=a[i]-b[j]
            if diff==target:
                return 1
            elif diff<target:
                i+=1
            else:
                j+=1
        return -1
                


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends