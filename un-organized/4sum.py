class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        temp = []
        for each in range(len(nums)):
           for sub_id in range(each, len(nums) -1):
               left = sub_id + 1
               right = len(nums) - 1
               while left < right:

                sum = nums[left] + nums[right] + nums[each] + nums[sub_id]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -=1
                else:
                    temp.append([nums[left], nums[right], nums[each], nums[sub_id]])
                    left += 1
                    right -= 1

        return temp





print(Solution().fourSum(nums= [1,0,-1,0,-2,2], target= 0))