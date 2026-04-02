from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        def check_doubles(board: List[str]):
            counter = Counter(board)
            for key in counter:
                if key == '.':
                    continue
                if counter[key]>1:
                    return True
            return False
        
        for row in board:
            if check_doubles(row):
                return False

        for i in range(n):
            col = ['.'] * n
            for j in range(n):
                col[j] = board[j][i]
            if check_doubles(col):
                return False
        i, j = 0, 0
        starting_cells = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                starting_cells.append([i,j])
        
        for s_cell in starting_cells:
            i, j = s_cell[0],s_cell[1]
            block = []
            for step_row in range(3):
                for step_col in range(3):
                    block.append(board[i+step_row][j+step_col])
            if check_doubles(block):
                return False
                
        
        return True