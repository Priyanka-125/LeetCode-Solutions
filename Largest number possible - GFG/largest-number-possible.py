#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        if S == 0 and N > 1:
            return -1
            
        ans = 0
        for i in range(N):
            if S > 9:
                ans = ans*10 + 9
                S -= 9
            else:
                ans = ans*10 + S
                S = 0
        return ans if S == 0 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends