class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        st=""
        for i in s:
            st+=i[::-1]+' '
        return st[:-1]    
        