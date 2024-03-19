def binary_search(s_array,target):
    left = 0
    right = len(s_array) - 1
    while left <= right:
        c_index = int((left + right)/2)
        check_target = s_array[c_index]
        if target < check_target:
            right -= 1
        elif target > check_target:
            left += 1
        else:
            return True
    return False

def binary_search_re(s_array, target, left, right):
    if left > right:
        return False
    c_index = int((left + right)/2)
    print(f" Array : {s_array[left:right]} \n left : {left}, \n right : {right} \n c_index : {c_index} \n c_value : {s_array[c_index] }")
    check_target = s_array[c_index]
   
    
    if target > check_target:
        left = c_index + 1
        right -= 1
        print("target is less so here")
        binary_search_re(s_array,target,left , right)
    elif target < check_target:
        right = c_index + 1
        left +=1
        print("target is greater so here")
        binary_search_re(s_array, target, left, right)
    else:
        print("am done")
        return target



if __name__ == "__main__":
    s_array = [0,3,5,6,8,11,15,17,19,21,22]
    target = 8
    print(binary_search(s_array=s_array, target=target))
    print(binary_search_re(s_array=s_array, target=target,left = 0, right = len(s_array) - 1))

