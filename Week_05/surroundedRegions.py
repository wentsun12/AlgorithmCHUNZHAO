
#dfs
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: retrun

        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                self._dfs(board,i,j)

        for i in range(len(board)):
            for j in [0, len(board[0])-1]:      
                self._dfs(board,i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='A':
                    board[i][j]='O'
    

    def _dfs(self, board, i, j):
        if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]=='O':
            board[i][j]='A'
            self._dfs(board,i+1,j)
            self._dfs(board,i-1,j)
            self._dfs(board,i,j-1)
            self._dfs(board,i,j+1)
