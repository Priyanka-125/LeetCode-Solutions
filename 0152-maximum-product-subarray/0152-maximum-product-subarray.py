class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max = nums[0]
        _min = nums[0]
        result = nums[0]
        for num in nums[1:]:
            _max *= num
            _min *= num
            _max, _min = max(_max, _min, num), min(_max, _min, num)
            result = max(result, _max)
        return result
        