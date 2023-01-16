#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        l=[]
        sub=""
        for i in range(len(S)):
            if S[i] not in sub:
                sub=sub+S[i]
            elif S[i] in sub:
                l.append(sub)
                sub=""
                x=S[:i].rfind(S[i])
                sub+=S[x+1:i+1]

        l.append(sub)
        maxx=0
        for i in l:
            if len(i)>maxx:
                maxx=len(i)
        return maxx
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends