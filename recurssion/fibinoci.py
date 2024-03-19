from timeit import repeat
import sys
from functools import lru_cache
   
mem = {}
@lru_cache
def fib(n):
    
    print(mem)
    if n <= 1:
        return n
    if n in mem:
        return mem[n]
    mem[n] = fib(n - 1) + fib(n - 2)
    return mem[n]
        
   
    
    
print(fib(4))