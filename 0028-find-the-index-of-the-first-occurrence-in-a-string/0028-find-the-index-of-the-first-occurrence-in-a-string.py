class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        subs=[]
        for i in range(len(haystack)-l+1):
            subs.append(haystack[i:i+l])
        print(subs)
        for i in range(len(subs)):
            if subs[i] == needle:
                return i
        return -1
        