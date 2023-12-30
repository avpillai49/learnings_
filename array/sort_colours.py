class Solution:
    
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        #TODO learn bucket sort
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num,0) + 1
        for nums_dict.
        print(nums_dict)
        """
        def swap(positon, i, nums):
            temp = nums[i]
            nums[i ]= nums[positon]
            nums[positon] = temp
            
        left = 0
        right = len(nums) - 1
        i = 0
        print(nums, right)
        while i <= right:
            if nums[i] == 0:
                swap(left,i,nums)
                left += 1
            if nums[i] == 2:
                swap(right, i , nums)
                print(nums)
                print("i just swapped right")
                right -= 1
                i -= 1
            i += 1
            print(left, right, i)
            print(nums)
            
            

nums =  [0,0,2,2,1,1]
Solution().sortColors(nums)