class Solution:
    def removeDuplicates(self, nums):

        i = 0
        j = 1
        
        while j <= len(nums) -1:
            if nums[i] == nums[j]:
                del nums[j]
            else:
             i += 1
             j += 1
           
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))

        