lista = [-2,-3,4,-1,-2, 1,5,-3]

def maxiumum_sub_array_sum(lista):
   currentsum = 0
   maxsum = -1e8
   n = len(lista)
   for i in range(0, n - 1):
    for j in range(i, n - 1):
        currentsum += lista[j]
        if currentsum > maxsum:
            maxsum = currentsum

    return maxsum

##KADANE ALOGORITHM  time (o(n)  space (o(1))
# )
def max_sub_array(lista):
    n = len(lista)
    maxsum = lista[0]
    currrentsum = 0
    for num in range(0, n-1):
        if currrentsum < 0:
            currrentsum = 0
        if currrentsum >= 0:
            currrentsum += lista[num]
        maxsum = max(maxsum, currrentsum)
    return maxsum

print(maxiumum_sub_array_sum(lista=lista)
)
print(max_sub_array(lista)
)


def maxSubArraySum(lista):
    n = len(lista)
    currentSum = 0
    maxSum = 0
    for i in range(n):
        currentSum += lista[i]
        if currentSum < 0:
            currentSum = 0
        elif currentSum >= 0:
            maxSum = max(maxSum, currentSum)
    return maxSum

def maxSubArraySumFinal(lista):
    import sys
    maxSum = -sys.maxsize -1
    currentSum = 0

    for i in lista:
        currentSum += i
        if currentSum < i:
            currentSum = i
        if maxSum <= currentSum:
            maxSum = currentSum
    return maxSum

print(maxSubArraySumFinal(lista=lista))

print(maxiumum_sub_array_sum(lista=lista)
)
print(max_sub_array(lista)
)
print(maxSubArraySum(lista))
