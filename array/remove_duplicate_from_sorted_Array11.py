class Solution:
    def removeDuplicates(self, nums):
         i = 0
         j = 1
         
         while j <= len(nums) -1:
              
              if j + 1 != len(nums) and nums[i] == nums[j] and nums[i]  == nums[j + 1]:
                  
                   del nums[j + 1]
              else:
                   i += 1
                   j += 1
             
         return len(nums)




nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))

        