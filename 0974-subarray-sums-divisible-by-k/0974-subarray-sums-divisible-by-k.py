class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        output = [0]*k
        prefix_mod = 0
        res = 0
        output[0] = 1
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i] % k + k) % k
            res = res + output[prefix_mod]
            output[prefix_mod] += 1
        return res