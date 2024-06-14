import time
import functools

def measure_runtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Function '{func.__name__}' took {runtime:.4f} seconds to complete.")
        return result
    return wrapper


class Solution():
    @measure_runtime
    def getJewls(self,jewels, stones):
        #brute force
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        
        return count
    @measure_runtime
    def getHashJewels(self, jewels, stones):
        dump = set(jewels)
        count = 0
        for i in stones:
            if i in dump:
                count += 1
        return count
    

jewels = "aA"
Stones = "aAAbbbb"
print(Solution().getJewls(jewels, Stones))
print(Solution().getHashJewels(jewels, Stones))