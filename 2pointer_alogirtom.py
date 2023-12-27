a = [1,2,3,4,5]

def swap(a):
    i = 0
    j = len(a) - 1
    while i < j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i = i+ 1
        j = j -1
    print(a)
swap(a)
