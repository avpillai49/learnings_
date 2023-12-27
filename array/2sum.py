class BruteSolution:
    
    def twoSum(self, nums , target: int) :
        
        for i in range(len(nums)):
            if (target - nums[i]) not in nums[:i]:
             print("returning", [i+1, nums.index((target-nums[i])) + 1] )
             continue
            else:
                return [i, nums.index(target - nums[i])]      

print(BruteSolution().twoSum([3,2,4], 6))


class HashSolution:
    def twoSum(self,nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i
        return []

print(HashSolution().twoSum([2,7,11,15], 9))