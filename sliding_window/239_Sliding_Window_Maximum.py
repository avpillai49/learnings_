#239. Sliding Window Maximum
from functools import reduce
from collections import deque
nums = [1,3,-1,-3,5,3,6,7]
k = 3
class Solution:
    def largest(self,arr):
           ans =  reduce(max, arr)
           return ans

    
   
    def maxSlidingWindow(self, nums  ,k: int) :
        output = []
        left, max = 0, 0
        right = k + left
        while right <= len(nums):
           
            output.append(self.largest(nums[left:right]))
            right += 1
            left += 1
        return output
    
    def maxSlidingWindowdeque(self, nums, k):
        res = []
        left = right = 0
        q = deque()
        print(nums)
        while right < len(nums):
            print(q, res)
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
           
            if left > q[0]:
                q.popleft()
            
            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1
        
        return res


    

            
print(Solution().maxSlidingWindowdeque(nums=nums, k = 3))
print(Solution().maxSlidingWindow(nums=nums, k = 3))