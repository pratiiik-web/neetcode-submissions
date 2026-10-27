class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(list(cur))
            if target <= 0:
                return

            prev = -1
            for i in range (pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return res