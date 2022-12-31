class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=[*set(nums)]
        l=[]
        nums.sort()
        n=len(nums)
        c=1
        i=1
        if (n==0 ):
            return 0
        elif(n==1):
            return 1
        for i in range(n):
            if (nums[i]==nums[i-1]+1):
                c+=1
                l.append(c)
            else:
                c=1
                continue
                
        print(l)
        return max(l,default=1)
        