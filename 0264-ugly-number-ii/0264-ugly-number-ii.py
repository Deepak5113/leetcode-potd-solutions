class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n  # To store ugly numbers
        ugly[0] = 1     # 1 is the first ugly number
        
        i2 = i3 = i5 = 0
        
        next_2 = 2
        next_3 = 3
        next_5 = 5
        
        for i in range(1, n):
            # Choose the smallest number among the next multiples
            next_ugly = min(next_2, next_3, next_5)
            ugly[i] = next_ugly
            
            if next_ugly == next_2:
                i2 += 1
                next_2 = ugly[i2] * 2
            if next_ugly == next_3:
                i3 += 1
                next_3 = ugly[i3] * 3
            if next_ugly == next_5:
                i5 += 1
                next_5 = ugly[i5] * 5
                
        return ugly[-1]