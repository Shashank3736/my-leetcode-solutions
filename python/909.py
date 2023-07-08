# Leetcode 909: Snakes and Ladders
# Language: Python 3
# https://leetcode.com/problems/snakes-and-ladders/

from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        print(board)
        def intToPos(i) -> [int, int]:
            i = i-1
            r = i // n
            c = i%n

            if r%2 == 0:
                # even row
                c = n - 1 - c
            
            return [r, c]
        
        q = deque()
        q.append([1, 0]) # [pos, moves]
        visit = set()

        while q:
            pos, moves = q.popleft()

            for i in range(pos+1, pos+7):
                [r, c] = intToPos(i)
                if i > n*n:
                    break
                print(r, c, i)
                if board[r][c] != -1:
                    i = board[r][c]
                if board[r][c] == n*n:
                    return moves + 1
                if i not in visit:
                    visit.add(i)
                    q.append([i, moves + 1])
        return -1
