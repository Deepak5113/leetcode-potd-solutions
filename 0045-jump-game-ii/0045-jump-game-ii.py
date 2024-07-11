class Solution:
    def jump(self, nums: List[int]) -> int:
        size=len(nums)
        i=0
        farthest=0
        current=0
        jump=0
        for i in range(size-1):
            farthest=max(farthest,nums[i]+i)
            if(i==current):
                current=farthest
                jump=jump+1
        return jump