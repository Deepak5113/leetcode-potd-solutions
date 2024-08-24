class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        
        # Edge cases for very small numbers
        if num == 0:
            return "1"
        if num == 1:
            return "0"
        
        # Handle corner cases like "1000", "999"
        candidates = set()
        candidates.add(str(10**(length - 1) - 1))  # largest number with one less digit (e.g., 999 for 1000)
        candidates.add(str(10**length + 1))        # smallest number with one more digit (e.g., 10001 for 9999)

        # Generate the palindrome by mirroring
        prefix = int(n[:(length + 1) // 2])
        for i in [-1, 0, 1]:
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)
        
        # Remove the original number from the candidates
        candidates.discard(n)
        
        # Find the closest palindrome
        closest = min(candidates, key=lambda x: (abs(int(x) - num), int(x)))
        
        return closest