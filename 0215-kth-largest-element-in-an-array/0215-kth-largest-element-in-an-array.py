class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums=nums[::-1]
        return nums[k-1]
    
        '''
        heap = nums[:k]
        print(heap)
        heapify(heap)                  #smallest to index[0] other element not necessarily arranged in order 
        print(heap)
        for n in nums[k:]:
            heappushpop(heap, n)       #pushes n and pop the largest element
            print(heap)
        return heap[0]
        '''