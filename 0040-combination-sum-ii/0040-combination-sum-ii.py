class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                # Add a copy of the current path because we'll continue to modify it
                result.append(path[:])
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates in the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include the current number and recurse
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                # Backtrack: remove the last added element
                path.pop()

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result
