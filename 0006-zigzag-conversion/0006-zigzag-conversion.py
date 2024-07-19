class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
    
        # Create an array of empty strings for each row
        rows = [''] * numRows
        cur_row = 0
        going_down = False
        
        # Traverse the string, appending characters to the appropriate row
        for char in s:
            rows[cur_row] += char
            # If we are at the top or bottom row, reverse the direction
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            # Move to the next row
            cur_row += 1 if going_down else -1
        
        # Concatenate all rows to get the final string
        return ''.join(rows)
