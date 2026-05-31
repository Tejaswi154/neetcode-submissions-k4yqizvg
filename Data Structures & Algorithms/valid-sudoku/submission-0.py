class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_seen=set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row_seen:
                    return False
                row_seen.add(board[i][j])

        for j in range(9):
            col_seen=set()
            for i in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in col_seen:
                    return False
                col_seen.add(board[i][j])
        for row in [0,3,6]:
            for col in [0,3,6]:
                box_seen=set()
                for i in range(row,row+3):
            
                    for j in range(col,col+3):
                        if board[i][j]=='.':
                            continue
                        if board[i][j] in box_seen:
                            return False
                        box_seen.add(board[i][j])


        
        return True        

                
        