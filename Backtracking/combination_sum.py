class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, combinations, total):
            if total == target:
                res.append(combinations.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            combinations.append(candidates[i])
            dfs(i, combinations, total + candidates[i])

            combinations.pop()
            dfs(i + 1, combinations, total)
        
        dfs(0, [], 0)
        return res