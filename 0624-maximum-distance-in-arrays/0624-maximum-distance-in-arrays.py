class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize the global minimum and maximum with the first array's elements
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        max_distance = 0
        
        # Traverse from the second array onwards
        for i in range(1, len(arrays)):
            # Current array's minimum and maximum
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]
            
            # Calculate possible maximum distance using the current array's min and max
            max_distance = max(max_distance, abs(curr_max - min_val), abs(max_val - curr_min))
            
            # Update the global minimum and maximum
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)
        
        return max_distance