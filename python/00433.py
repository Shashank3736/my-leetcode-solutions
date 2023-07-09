# Leetcode 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
# Difficulty: Medium

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        def isMutation(g1, g2):
            diff = 0
            for i in range(len(g1)):
                if g1[i] != g2[i]:
                    diff += 1
            return diff == 1
        
        queue = [(startGene, 0)]
        visited = set()
        while queue:
            gene, steps = queue.pop(0)
            if gene == endGene:
                return steps
            for b in bank:
                if b not in visited and isMutation(gene, b):
                    visited.add(b)
                    queue.append((b, steps+1))
        
        return -1