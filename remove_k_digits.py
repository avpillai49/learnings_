def removeKdigits( num: str, k: int) -> str:
    stack = []
    for each in num:
        print(stack)
        print(k)
        # Pop element from stack if the current element is smaller than last added element in stack
        while k and stack and stack[-1] > each:
            stack.pop()
            k -= 1
        stack.append(each)

    # If still k elements left to remove, then remove them from the stack.
    #while k > 0:
    #    stack.pop()
    #    k -= 1
    # Remove leading zeros
    output = "".join(stack).lstrip("0")

    return (output if output else "0")
num = "1432219"
k = 3
print(removeKdigits(num, k))
