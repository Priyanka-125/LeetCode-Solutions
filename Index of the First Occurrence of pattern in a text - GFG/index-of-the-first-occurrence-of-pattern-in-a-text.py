#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def findMatching(self, text, pattern):
        # Code here
        '''
        if pattern=="": return 0
        for i in range(len(text)-len(pattern)+1):
            if text[i:i+len(pattern)]==pattern:
                return i
        return -1
        '''
        a=''
        if pattern not in text:
            return -1
        for i in range(len(text)-len(pattern)+1):
            for j in range(len(pattern)):
                a+=text[i+j]
                if a==pattern:
                    return i
            a=''

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        text, pattern = input().split()
        ob = Solution()
        res = ob.findMatching(text, pattern)
        print(res)
# } Driver Code Ends