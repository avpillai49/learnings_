class Solution:
    def max_sub_array(self,num_list:list, k:int) -> int:
        sum = 0
        Csum = 0
        left, right = 0, 0
        visit = set()
        while right < len(num_list):
            while num_list[right] in visit:
                Csum -= num_list[left]
                print(num_list[left:right], Csum)
                visit.remove(num_list[left])
                left += 1
            Csum += num_list[right]
            visit.add(num_list[right])

            if (right - left + 1) == k:
                sum = max(Csum, sum)
                Csum -= num_list[left]
                visit.remove(num_list[left])
                left += 1
            right += 1
 
        return sum
    
print(Solution().max_sub_array([1, 5, 4, 2, 9, 9, 9],3))