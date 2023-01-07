class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        c=1
        n=len(b)
        t=a
        while t!=b and len(t)<=n:
            c=c+1
            t=a*c
        if b in t:
            return c
        if b in a*(c+1):
            return c+1
        else:
            return -1
            
        