class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the pointer for the unique elements
        i = 0
        
        # Iterate through the array starting from the second element
        for j in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[j] != nums[i]:
                # Move the pointer for unique elements and update the value
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements is i + 1
        return i + 1