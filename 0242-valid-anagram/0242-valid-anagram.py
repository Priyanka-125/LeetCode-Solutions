class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if len(s)==len(t):
            for i in s:
                if s.count(i)!=t.count(i):
                    return False
        
        return True
    
    '''
    def isAnagram(self,a,b):
        if sorted(a)==sorted(b):
            return True
        else:
            return False
    '''
        