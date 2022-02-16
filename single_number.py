class Solution:
    def singleNumber(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        i = 0
        while i < len(nums) :
            if i == len(nums) - 1 :
                return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2
        return -1

print(Solution().singleNumber([4,1,2,1,2]))

