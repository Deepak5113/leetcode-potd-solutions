class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        sum=0
        for i in range(0,len(s),2):
            sum+=ord(s[i])-ord('0')
        for i in range(1,len(s),2):
            sum-=ord(s[i])-ord('0')
        return sum