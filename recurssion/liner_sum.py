sums = 0
def liner_sum(nums,sums, n):
    if n == 0:
        return sums
    sums += nums[n - 1]
    return liner_sum(nums, sums, n - 1)
    

nums = [1,3,4,3]
print(liner_sum(nums,sums,len(nums)))