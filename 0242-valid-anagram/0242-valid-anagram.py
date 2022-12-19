class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt=0
        if len(s)!=len(t):
            return False
        for i in s:
            if s.count(i)!=t.count(i):
                return False
        else:
            return True
        