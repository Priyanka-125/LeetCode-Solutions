class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        z= zip(s,t)
        if len(set(z))==len(set(s))==len(set(t)):
            return True
        return False
        