from functools import lru_cache
@lru_cache
def print_1_n(n):
    print(f"am here and n is  {n}")
    if n == 0:
        return
    print_1_n(n - 1)
    print(n)

print_1_n(9)