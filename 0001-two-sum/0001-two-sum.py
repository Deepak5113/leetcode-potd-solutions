class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store the value and its index
        num_map = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement that would add up to the target
            complement = target - num
            
            # If the complement exists in the dictionary, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the current number with its index in the dictionary
            num_map[num] = i