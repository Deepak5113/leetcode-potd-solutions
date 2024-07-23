from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each element
        freq = Counter(nums)
        
        # Step 2: Sort the elements based on frequency and value
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums