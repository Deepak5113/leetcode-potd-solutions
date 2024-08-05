class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Dictionary to store the count of each string
        count = {}
        
        # Count occurrences of each string
        for s in arr:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        
        # List to store distinct strings
        distinct_strings = []
        
        # Identify distinct strings by maintaining the order of appearance
        for s in arr:
            if count[s] == 1:
                distinct_strings.append(s)
        
        # Check if we have at least k distinct strings
        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""