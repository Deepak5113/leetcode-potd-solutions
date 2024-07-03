class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #if length of nums is less than four then the result will always 0 
        #bcoz from 4 elements 3 will be removed and min difference of same number is 0.
        if len(nums)<=4:
            return 0
        nums.sort()
        result=float('inf')
        for l in range(4):
            r=len(nums)-4+l
            result=min(result,nums[r]-nums[l])
            
        return result
            