class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        i = 0
        while i < n:
            i += 1
            n -= i
            print(i, n)
        return i

print(Solution().arrangeCoins(5))
