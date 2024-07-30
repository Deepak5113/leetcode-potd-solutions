class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
    
        # Arrays to store prefix and suffix counts
        prefix_b_count = [0] * (n + 1)
        suffix_a_count = [0] * (n + 1)
        
        # Fill prefix_b_count
        for i in range(1, n + 1):
            prefix_b_count[i] = prefix_b_count[i - 1] + (1 if s[i - 1] == 'b' else 0)
        
        # Fill suffix_a_count
        for i in range(n - 1, -1, -1):
            suffix_a_count[i] = suffix_a_count[i + 1] + (1 if s[i] == 'a' else 0)
        
        # Calculate minimum deletions
        min_deletions = float('inf')
        for i in range(n + 1):
            min_deletions = min(min_deletions, prefix_b_count[i] + suffix_a_count[i])
        
        return min_deletions
