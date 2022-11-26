class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r = []
        w = []
        b = []

        for i in range(len(nums)):
            if nums[i] == 0:
                r.append(0)

            if nums[i] == 1:
                w.append(1)

            if nums[i] == 2:
                b.append(2)
	
        nums.clear()
        nums.extend(r)
        nums.extend(w)
        nums.extend(b)
        