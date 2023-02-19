class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if len(s)!=len(t):
            return False
        if len(s)==len(t):
            for i in s:
                if s.count(i)!=t.count(i):
                    return False
        
        return True
    
    
    def isAnagram(self,a,b):
        if sorted(a)==sorted(b):
            return True
        else:
            return False
    '''
        res1=dict()
        res2=dict()
        for i in s:
            if i not in res1:
                res1[i]=1
            else:
                res1[i]+=1
        for i in t:
            if i not in res2:
                res2[i]=1
            else:
                res2[i]+=1
        return res1==res2
        
        