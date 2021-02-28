#tired

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.dx =[-1,1,0,0]
        self.dy =[0,0,-1,1]


        if not board or not board[0]:return[]
        if not words: return []
        self.res = set()

        #构建trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node=node.setdefault(char, {})
            node["#"] = True

        #dfs
        self.m, self.n = len(board),len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in trie:
                    self._dfs(board, i, j,"",trie)
        return list(self.res)

    def _dfs(self, board,i,j,cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if "#" in cur_dict:
            self.res.add(cur_word)
        tmp,board[i][j]= board[i][j], "@"
        for k in range(4):
            x, y = i+self.dx[k], j+self.dy[k]
            if 0<=x<self.m and 0<=y<self.n and board[x][y] !="@" and board[x][y] in cur_dict:
                self._dfs(board,x,y,cur_word,cur_dict)
        board[i][j] = tmp
