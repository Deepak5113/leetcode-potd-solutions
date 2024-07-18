class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Trim the string to remove leading and trailing spaces
        s = s.strip()
        
        # Step 2: Split the string into words based on spaces
        words = s.split()
        
        # Step 3: Reverse the list of words
        words.reverse()
        
        # Step 4: Join the reversed list of words with a single space between them
        reversed_string = ' '.join(words)
        
        return reversed_string