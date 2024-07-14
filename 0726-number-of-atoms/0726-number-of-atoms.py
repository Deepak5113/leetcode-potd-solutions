from collections import defaultdict, deque
import re
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = deque()
        stack.append(defaultdict(int))
        
        i, n = 0, len(formula)
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[start:i] or 1)
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplicity
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[start:i] or 1)
                stack[-1][atom] += multiplicity
        
        # Get the final counts from the stack
        final_counts = stack.pop()
        
        # Create the result string
        result = []
        for atom in sorted(final_counts):
            count = final_counts[atom]
            result.append(atom)
            if count > 1:
                result.append(str(count))
        
        return ''.join(result)