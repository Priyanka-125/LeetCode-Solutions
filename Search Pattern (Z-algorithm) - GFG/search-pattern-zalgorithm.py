#User function Template for python3

class Solution:
    def search(self, patt, s):
        # code here
        t=patt[0]
        k=[]
        for i in range(len(s)):
            if s[i]==t:
                if s[i:i+len(patt)]==patt:
                    k.append(i+1)
        if len(k)>0:
            return k
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
        if len(ans)==0:
            print("-1", end = " ")
        else:
            for value in ans:
                print(value,end = ' ')
        print()
# } Driver Code Ends