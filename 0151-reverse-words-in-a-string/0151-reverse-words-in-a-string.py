class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        l=[]
        for i in reversed(range(0,len(s))):
            l.append(s[i])
        return ' '.join(l)

        