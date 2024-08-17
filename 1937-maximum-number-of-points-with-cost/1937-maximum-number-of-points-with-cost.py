class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
    
        # Initialize the dp array with the first row of points
        dp = points[0]
        
        # Process each row
        for i in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            
            # Compute the left max values
            left_max[0] = dp[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j-1] - 1, dp[j])
            
            # Compute the right max values
            right_max[n-1] = dp[n-1]
            for j in range(n-2, -1, -1):
                right_max[j] = max(right_max[j+1] - 1, dp[j])
            
            # Update dp for the current row
            for j in range(n):
                dp[j] = points[i][j] + max(left_max[j], right_max[j])
        
        # The maximum value in dp array is the result
        return max(dp)
