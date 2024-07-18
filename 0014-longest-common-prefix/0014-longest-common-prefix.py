class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Iterate over the other strings
        for string in strs[1:]:
            # Compare the prefix with each string and update
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
            
            # If the prefix becomes empty, no common prefix exists
            if not prefix:
                return ""
        
        return prefix