class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row, column, and box separately

        # check each row
        for row in range(9):
            row_set = set()
            for col in range(9):
                if board[row][col] in row_set:
                    return False
                elif board[row][col] != ".":
                    row_set.add(board[row][col])

        
        # check each column
        for col in range(9):
            col_set = set()
            for row in range(9):
                if board[row][col] in col_set:
                    return False
                elif board[row][col] != ".":
                    col_set.add(board[row][col])

        # box is a bit more difficult, will have to keep a hashmap
        # key is which of the 9 boxes it is in
        # value is just the element
        box_hashmap = defaultdict(set)
        for row in range(9):
            for col in range(9):
                # check which box we are currently in
                box = (row // 3, col // 3)
                if board[row][col] in box_hashmap[box]:
                    return False
                elif board[row][col] != ".":
                    box_hashmap[box].add(board[row][col])
        
        return True
'''
Time Complexity: O(1) -> we have to check each condition separately so we have to look over the whole board 3 times. However, the problem specifies that the board will always be a 9x9 matrix so it will always run in constant time, since the input size doesn't vary. If it did vary and the function took in a nxn matrix, the time complexity would be O(n^2)

Space Complexity: O(1) -> the space complexity is dominated by the hashmap, which could end up holding all 81 elements. Same concept as before, if it was an nxn matrix, the space complexity would be O(n^2)
'''


        