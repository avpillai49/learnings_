givensum = 33
lista = [1,3,20,3,10,5]
def subarraywithgivensum(givenSum, nums):
    left, right, currentSum = 0,0,0
    for i in range(len(nums)):
        currentSum += nums[i]
        
        if currentSum < givenSum:
            right += 1
        if currentSum > givenSum:
            currentSum = currentSum - nums[left]
            left += 1
        print(nums[i],currentSum,left,right)
    return nums[left:right]

print(subarraywithgivensum(givenSum=givensum, nums=lista)) 
