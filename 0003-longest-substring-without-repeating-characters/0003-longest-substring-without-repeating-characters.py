class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        res = 0
        l = 0
        for r in range(len(s)): 
            while s[r] in charset:
                charset.remove(s[l])
                l+=1  
            charset.add(s[r])
            print(charset)
            res = max(res,r-l+1)
        return res
    
    '''
    l = []
    count = 0
    i = 0
    while (i<len(s)):
        if s[i] not in l:
            l.append(s[i])
            i += 1
        else:
            if s[i] == l[0]:
                count = max(count, len(l))
                l.pop(0)
            else:
                count = max(count, len(l))
                while s[i] != l[0]:
                    l.pop(0)
    count = max(count,len(l))
    return count
    '''