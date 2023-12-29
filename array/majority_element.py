class Solution:
    def majorityElement(self, nums):
        hash_Dict = {}
        for num in nums:
            hash_Dict[num] = hash_Dict.get(num, 0) + 1
            if hash_Dict[num] > len(nums) //2:
                return num


