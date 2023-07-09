# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# Difficulty: Medium
# Approach: DFS

import collections


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        def dfs(u, p):
            res = 0
            for v, w in graph[u]:
                if v != p:
                    res += w + dfs(v, u)
            return res
        return dfs(0, -1)