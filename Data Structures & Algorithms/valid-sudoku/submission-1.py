class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check Rows
        for i in range(9):
            seen = set()
            for j in range(9):
                
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in seen:
                    return False
                    
                seen.add(board[i][j])
        
        #Check cols
        for j in range(9):
            seen = set()
            for i in range(9):
                
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in seen:
                    return False
                    
                seen.add(board[i][j])
        
        
        #Check Grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                
                for r in range(3):
                    for c in range(3):
                        
                        if board[i+r][j+c] == '.':
                            continue
                        
                        if board[i+r][j+c] in seen:
                            return False
                               
                        seen.add(board[i+r][j+c])


        return True