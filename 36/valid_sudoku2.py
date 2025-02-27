class Solution:

    def is_repeated(self, nums: list[str]) -> bool:
        num_set = set()
        for num in nums:
            if num!=".":
                if num in num_set:
                    return True
                num_set.add(num)

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for i in range(9):
            row = board[i]
            col = [el[i] for el in board]
            box = []
            for j in range(3):
                row_index = i//3*3 +j
                col_index = i%3*3,i%3*3+3
                box.extend(
                    board[row_index][col_index[0]:col_index[1]]
                )
            if self.is_repeated(row) or self.is_repeated(col) or self.is_repeated(box):
                return False
        return True


print(Solution().isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))