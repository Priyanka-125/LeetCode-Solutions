class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        L, S = len(str1), len(str2)
        
        for i in range(S, 0, -1):
            if (L/i) == int(L/i) and (S/i) == int(S/i):
                c = str2[:i]
                if c*int(L/i) == str1 and c*int(S/i) == str2: 
                    return c
                
        return ""