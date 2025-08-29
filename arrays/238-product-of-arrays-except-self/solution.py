class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # left = [1] * n
        
        # for i in range(1, n):
        #     left[i] = left[i - 1] * nums[i - 1]

        # right = [1] * n
        # for i in range(n - 2, -1, -1):
        #     right[i] = right[i + 1] * nums[i + 1]

        # res = [1] * n
        # for i in range(n):
        #     res[i] = left[i] * right[i]

        # return res

        # optimal
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
    
    - Input: nums = [1,2,3,4]
- Output: [24,12,8,6]