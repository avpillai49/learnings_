def factorial(n):
    if  n ==0 :
        return n
    res = 1
    for i in range(1,n+1):
        res = res*i
    return res

def re_factorial(n):
    if n ==0 :
        return 1
    print(n)
    return n * re_factorial(n -1)
    

if __name__ == "__main__":
    print(re_factorial(3))
