class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_row = [min(row) for row in matrix]

        # Step 2: Find the maximum element in each column
        max_in_col = [max(col) for col in zip(*matrix)]

        # Step 3: Find all elements that are both in min_in_row and max_in_col
        lucky_numbers = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_in_row[i] and matrix[i][j] == max_in_col[j]:
                    lucky_numbers.append(matrix[i][j])
        
        return lucky_numbers
