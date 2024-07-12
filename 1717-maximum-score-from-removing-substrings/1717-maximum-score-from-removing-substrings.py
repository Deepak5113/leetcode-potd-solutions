class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n=len(s)
        totalScore=0
        if x>y:
            highPriorityPair="ab"
            lowPriorityPair="ba"
        else:
            highPriorityPair="ba"
            lowPriorityPair="ab"
        # First pass: remove high priority pair
        s1=self.removeSubstring(s,highPriorityPair)
        removedPairCount=(n-len(s1))//2
        # Calculate score from first pass
        totalScore+=removedPairCount*max(x,y)
        # Second pass: remove low priority pair
        s2=self.removeSubstring(s1,lowPriorityPair)
        removedPairCount=(len(s1)-len(s2))//2
        # Calculate score from second pass
        totalScore+=removedPairCount*min(x,y)
        return totalScore

    def removeSubstring(self, input, targetPair):
        charStack=[]
        for c in input:
            if charStack and charStack[-1] == targetPair[0] and c == targetPair[1]:
                charStack.pop()
            else:
                charStack.append(c)
        return ''.join(charStack)

