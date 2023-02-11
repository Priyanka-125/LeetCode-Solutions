#User function Template for python3

class Solution:
    def search(self, patt, s):
        # code here
        t=patt[0]
        b=[]
        for i in range(len(s)):
            if(s[i]==t):
                k=s[i:i+len(patt)]
                if(k==patt):
                    b.append(i+1)
        if(len(b)>0):
            return b
        else:
            return [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends