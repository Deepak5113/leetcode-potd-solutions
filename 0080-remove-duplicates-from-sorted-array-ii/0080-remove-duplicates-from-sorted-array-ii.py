class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # Initialize the pointer for the position of the unique elements
        i = 1
        
        # Iterate through the array starting from the third element
        for j in range(2, len(nums)):
            # If the current element is different from the element at index i-1
            if nums[j] != nums[i - 1]:
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements that can appear at most twice is i + 1
        return i + 1