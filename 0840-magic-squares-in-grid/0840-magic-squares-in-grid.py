class Solution:
    def is_magic(self, square):
        # The sum for a 3x3 magic square is always 15
        magic_sum = 15
        
        # Check if all elements are unique and from 1 to 9
        elements = [square[i][j] for i in range(3) for j in range(3)]
        if sorted(elements) != list(range(1, 10)):
            return False
        
        # Check row sums
        for i in range(3):
            if sum(square[i]) != magic_sum:
                return False
        
        # Check column sums
        for j in range(3):
            if sum(square[i][j] for i in range(3)) != magic_sum:
                return False
        
        # Check diagonal sums
        if square[0][0] + square[1][1] + square[2][2] != magic_sum:
            return False
        if square[0][2] + square[1][1] + square[2][0] != magic_sum:
            return False
        
        return True

    def numMagicSquaresInside(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        # Slide a 3x3 window over the grid
        for i in range(rows - 2):
            for j in range(cols - 2):
                # Extract the 3x3 subgrid
                square = [row[j:j+3] for row in grid[i:i+3]]
                if self.is_magic(square):  # Note the use of 'self'
                    count += 1
        
        return count