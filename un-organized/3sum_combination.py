class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        temp = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) -1
            x = nums[i]
            print(x)
            while left < right:
                if x + nums[left] + nums[right] == 0:
                    temp.append([nums[left], nums[right],x])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif x + nums[left] + nums[right] < 0:
                    left +=1
                else:
                    right -=1
            print(temp)

        return temp


print(Solution().threeSum(nums=[-1,0,1,2,-1,-4]))