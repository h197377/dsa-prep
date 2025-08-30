class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return 
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                used[i] = False
                
        res = []
        used = [False] * len(nums)
        backtrack([])
        return res