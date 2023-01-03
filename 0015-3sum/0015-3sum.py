class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trip=[]
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                currsum=0
                currsum=nums[i]+nums[left]+nums[right]
                if currsum==0:
                    trip.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                elif currsum < 0:
                    left += 1 
                else:
                    right -= 1
        res = list(set(tuple(sub) for sub in trip))
        return res
        