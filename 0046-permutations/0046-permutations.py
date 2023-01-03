class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n in [0, 1]:
            return [nums]
        if n == 2:
            return [nums, nums[::-1]]
			
        res = []
		
        for i in range(n):
            permutations = self.permute(nums[:i] + nums[i+1:])
            for p in permutations:
                res.append([nums[i]] + p)
				
        return res
        