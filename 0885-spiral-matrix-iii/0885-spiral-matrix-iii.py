class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        
        total_cells = rows * cols
        step = 1  # Initial step count in each direction
        
        r, c = rStart, cStart
        result.append([r, c])
        
        direction_index = 0  # Start moving east
        
        while len(result) < total_cells:
            # Move in the current direction
            for _ in range(2):  # Increase step size every two directions
                dr, dc = directions[direction_index % 4]
                for _ in range(step):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                direction_index += 1
            step += 1  # Increase step size after two turns
        
        return result
