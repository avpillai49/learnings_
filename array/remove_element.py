class Solution:
    def removeElement(self, nums, val):

        i = 0
        res = 0
        while i <= len(nums) - 1:
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
        