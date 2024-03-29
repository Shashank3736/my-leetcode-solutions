# 130. Surrounded Regions
#-------------------------------------------------------------------------------
# https://leetcode.com/problems/surrounded-regions/
#-------------------------------------------------------------------------------
# Solution Approach:

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        
        for i in range(cols):
            dfs(0, i)
            dfs(rows-1, i)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
