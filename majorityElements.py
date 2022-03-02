def majorityElemt(nums):
    count = 1
    current = nums[0]
    for i in nums[1:]:
        count += (1 if current == i else -1)
        if not count:
            current = i
            count = 1
    return count

print((majorityElemt([1,1,2,3,1])))