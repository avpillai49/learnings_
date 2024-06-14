class Solution:
    def maxScore(self, nums, k):
        left = 0
        right = len(nums) - k
        total = sum(nums[k:])
        res = 0
        while right < len(nums):
            total += nums[left] - nums[right]
            res = max(res, total)
            left += 1
            right += 1
        return res

k = 3
nums = [1,2,3,2,3,4,5,6,2,2,1]
print(Solution().maxScore(nums,k))


