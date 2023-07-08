# Leetcode 909: Snakes and Ladders
# Language: Python 3
# https://leetcode.com/problems/snakes-and-ladders/

from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def intToPos(i):
            r = (i - 1) // n
            c = (i - 1) % n
            if r % 2:
                # even row
                c = n - 1 - c
            return [r, c]
        
        q = deque()
        q.append([1, 0]) # [pos, moves]
        visit = set()
        while q:
            pos, moves = q.popleft()
            for i in range(1, 7):
                npos = pos + i
                r, c = intToPos(npos)
                if board[r][c] != -1:
                    npos = board[r][c]
                if npos == n*n:
                    return moves + 1
                if i not in visit:
                    visit.add(i)
                    q.append([i, moves + 1])
        return -1
