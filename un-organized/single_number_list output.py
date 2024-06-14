class Solution:
   def singlenumber_f(self,nums):
       temp = {}

       for i in nums:
           if  i in temp:
               del temp[i]
           else:
               temp[i] = 1
       return list(temp.keys())


a = [0,1,1,2]
print(Solution().singlenumber_f(a))