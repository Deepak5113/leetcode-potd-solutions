class Solution:
    from math import gcd
    from functools import reduce

    def lcm(a, b):
        return a * b // gcd(a, b)

    def add_fractions(self,num1, den1, num2, den2):
        common_den = lcm(den1, den2)
        num1 *= (common_den // den1)
        num2 *= (common_den // den2)
        return num1 + num2, common_den

    def simplify_fraction(self, numerator, denominator):
        common_divisor = gcd(abs(numerator), abs(denominator))
        return numerator // common_divisor, denominator // common_divisor

    def fractionAddition(self, expression: str) -> str:
        i, n = 0, len(expression)
        num, den = 0, 1  # Initialize to 0/1 as the starting fraction

        while i < n:
            sign = 1
            if expression[i] == '+' or expression[i] == '-':
                if expression[i] == '-':
                    sign = -1
                i += 1
            
            num_start = i
            while i < n and expression[i] != '/':
                i += 1
            numerator = int(expression[num_start:i]) * sign
            
            i += 1
            den_start = i
            while i < n and expression[i].isdigit():
                i += 1
            denominator = int(expression[den_start:i])
            
            num, den = self.add_fractions(num, den, numerator, denominator)
            num, den = self.simplify_fraction(num, den)

        return f"{num}/{den}"
