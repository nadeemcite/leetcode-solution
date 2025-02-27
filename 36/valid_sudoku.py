class Solution(object):
    def check_repetition(self, nums):
        num_set = set()
        for num in nums:
            if num != "." and num in num_set:
                return True
            elif num != ".":
                num_set.add(num)
        return False

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = board[i]
            col = [el[i] for el in board]
            box = []
            for j in range(3):
                row_index = (i//3)*3 + j
                row_range = (i%3*3, (i%3*3)+3)
                target_box = board[row_index][row_range[0]:row_range[1]]
                box.extend(target_box)

            if self.check_repetition(row) or self.check_repetition(col) or self.check_repetition(box):
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
        