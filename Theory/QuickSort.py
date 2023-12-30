def quick_sort(sequence):

    length = len(sequence)
    if length <= 1:
        return sequence
    
    pivot = sequence.pop()
    item_lower = []
    item_bigger = []
    for item in sequence:
        if item < pivot:
            item_lower.append(item)
        else:
            item_bigger.append(item)
    return quick_sort(item_lower) + [pivot] + quick_sort(item_bigger)

sequence = [1,2,1,3,5,4,6,8,1,3,44]
print(quick_sort(sequence))