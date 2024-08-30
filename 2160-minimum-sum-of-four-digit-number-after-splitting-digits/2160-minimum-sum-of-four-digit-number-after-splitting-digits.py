class Solution:
    def minimumSum(self, num: int) -> int:
        s=sorted(str(num))
        last=int(s[3])
        second_last=int(s[2])
        num1=(int(s[0])*10+last)
        num2=(int(s[1])*10+second_last)
        return num1+num2
 