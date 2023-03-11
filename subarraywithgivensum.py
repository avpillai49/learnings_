givensum = 33
lista = [1,3,20,3,10,5]
currentSum,left, right = 0,0,0

for i in range(len(lista)):
    currentSum += lista[i]
    if currentSum < givensum:
        right +=1
    if currentSum > givensum:
        left += 1
print(lista[left::right])


