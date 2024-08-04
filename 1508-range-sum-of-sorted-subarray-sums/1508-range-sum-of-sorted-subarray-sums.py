class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Step 1: Compute all subarray sums
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        
        # Step 2: Sort the subarray sums
        subarray_sums.sort()
        
        # Step 3: Compute the sum in the range [left, right]
        # Convert 1-based index to 0-based index
        left -= 1
        right -= 1
        result_sum = sum(subarray_sums[left:right + 1]) % MOD
        
        return result_sum