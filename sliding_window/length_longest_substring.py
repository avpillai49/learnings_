s = "tmmzuxt"
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        seen = {}
        length, left = 0, 0
        for right in range(len(s)):
            char = s[right]
            if char not in seen:
                length = max(length, right - left + 1)
            else:
                if seen[char] >= left:
                    left = seen[char]
            seen[char] = right
        return length
                
print(Solution().lengthOfLongestSubstring(s))