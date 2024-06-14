from sortedcontainers import SortedList
class Solutions:
    def sub_array_beauty(self, nums, k, x):
       op = []
       i = 0
       j = i + k
       temp = SortedList(nums[i:j])
       print(temp)
       op.append(min(0, temp[x - 1])) 
       while j < len(nums):
           print(temp)
           temp.remove(nums[i])
           temp.add(nums[j])
           op.append(min(0, temp[x - 1])) 
           i += 1
           j = i + k
       return op
           
           

nums = [1,-1,-3,-2,3]
k = 3
x = 2
print(Solutions().sub_array_beauty(nums,k,x))