from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1=s1.split()
        words2=s2.split()
        count1=Counter(words1)
        count2=Counter(words2)
        combined_count=count1+count2
        uncommon_words=[word for word,count in combined_count.items() if count==1]
        return uncommon_words
        
            
            