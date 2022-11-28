class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i]==nums[i+1]:
                    return nums[i]
        