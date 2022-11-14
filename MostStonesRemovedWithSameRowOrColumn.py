# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = {}
        i = 0
        for s in stones:
            visited[s[0], s[1]] = False
        
        for stone in stones:
            if not visited[stone[0], stone[1]]:
                self.dfs(stone, visited, stones)
                i += 1

        return len(stones) - i


    
    def dfs(self, stone, visited, stones):
        visited[stone[0], stone[1]] = True
        for nextStone in stones:
            if not visited[nextStone[0], nextStone[1]] and (nextStone[0] == stone[0] or nextStone[1] == stone[1]):
                self.dfs(nextStone, visited, stones)
