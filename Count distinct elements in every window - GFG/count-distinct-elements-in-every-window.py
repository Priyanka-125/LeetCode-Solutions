
class Solution:
    def countDistinct(self, A, N, K):
        m = {}
        for i in range(K):
            if A[i] in m:
                m[A[i]] += 1
            else:
                m[A[i]] = 1
        
        result = [len(m)]
        i = K
        while i<N:
            if m[A[i-K]] == 1:
                del m[A[i-K]]
            else:
                m[A[i-K]] -= 1
                
            if A[i] in m:
                m[A[i]] += 1
            else:
                m[A[i]] = 1
                
            result.append(len(m))
            i+=1
            
        return result
                


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends