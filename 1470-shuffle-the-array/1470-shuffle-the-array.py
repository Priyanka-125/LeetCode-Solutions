class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        k=[]
        p=[]
        for i in range(len(nums)//2):
            l.append(nums[i])
        for i in range(n,len(nums)):
            k.append(nums[i])
        for i in range(len(nums)//2):
            p.append(l[i])
            p.append(k[i])
        return p
    '''
    ls=[]
        for i in range(n):
            ls+=[nums[i]]
            ls+=[nums[i+n]]
        return ls
    '''