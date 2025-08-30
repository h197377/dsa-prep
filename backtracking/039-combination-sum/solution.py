class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(res, i, curr_sum, nums):
            if curr_sum == target:
                res.append(nums[:])
                return 
            if curr_sum > target:
                return 
            
            for idx in range(i, len(candidates)):
                # explicit backtracking
                # nums.append(candidates[idx])
                # backtrack(res, idx, curr_sum + candidates[idx], nums)
                # nums.pop()
                backtrack(res, idx, curr_sum + candidates[idx], nums + [candidates[idx]])
        
        candidates.sort()
        res = []
        backtrack(res, 0, 0, [])
        return res