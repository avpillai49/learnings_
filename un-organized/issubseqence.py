class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) > len(t):
            return False
        if len(s) == len(t) and s != t:
            return False
        while i < len(s):
            if s[i] not in t:
                return False
            index = t.index(s[i]) + 1
            t = t[index:]
            print(t)
            i += 1
        return True

s ='bb'
t = 'ahbgdc'
print(Solution().isSubsequence(s,t))