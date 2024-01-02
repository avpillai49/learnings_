class Solution:
     def canJump(self, nums):
          
          goal = 0
          for i , x in enumerate(nums):
               if i > goal:
                    return False
               goal = max(goal, i + x)
          return True
     
     def canJumpDP(self,nums):
          goal = len(nums) - 1
          
        
        
      
            
          
                    



       
nums = [3,0,8,2,0,0,1]
print(Solution().canJump(nums))
        