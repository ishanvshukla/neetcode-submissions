class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row, column, and box separately

        for row in range(len(board)):
            row_set = set()
            for col in range(len(board[0])):
                
                if board[row][col] in row_set:
                    return False
                elif board[row][col] != ".":
                    row_set.add(board[row][col])

        

        for col in range(len(board[0])):
            col_set = set()
            for row in range(len(board)):
                if board[row][col] in col_set:
                    return False
                elif board[row][col] != ".":
                    col_set.add(board[row][col])

        # box is a bit more difficult, will have to keep a hashmap
        # key is which of the 9 boxes it is in
        # value is just the element
        box_hashmap = defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board[0])):
                box_row = row // 3
                box_col = col // 3
                box = (box_row, box_col)
                if board[row][col] in box_hashmap[box]:
                    return False
                elif board[row][col] != ".":
                    box_hashmap[box].append(board[row][col])
        
        return True


        