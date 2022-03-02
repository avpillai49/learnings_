class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for each in range(max(v1, v2)):
            v1_item = int(v1[each]) if len(v1)> each else 0
            v2_item = int(v2[each]) if len(v2) > each else 0
            if v1_item > v2_item : return 1
            if v2_item > v1_item : return -1
        return 0