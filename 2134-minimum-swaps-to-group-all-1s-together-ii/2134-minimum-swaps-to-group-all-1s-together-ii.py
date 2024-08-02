class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        countOnes = nums.count(1)

        # Handle edge cases
        if countOnes == 0 or countOnes == n:
            return 0

        # Extend the array to handle the circular nature
        extended_nums = nums + nums

        # Initialize the number of 1's in the current window
        currentOnes = sum(extended_nums[:countOnes])
        maxOnesInWindow = currentOnes

        # Use sliding window to find the max number of 1's in any window of size countOnes
        for i in range(1, n):
            currentOnes = currentOnes - extended_nums[i - 1] + extended_nums[i + countOnes - 1]
            maxOnesInWindow = max(maxOnesInWindow, currentOnes)

        # The minimum swaps needed is the difference between countOnes and maxOnesInWindow
        minSwaps = countOnes - maxOnesInWindow

        return minSwaps