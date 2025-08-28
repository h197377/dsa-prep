class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        running = nums[0]
        res = running

        for i in range(1, len(nums)):
            running = max(nums[i], running + nums[i])
            res = max(res, running)

        return res