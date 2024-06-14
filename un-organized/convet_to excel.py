class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = range(1, 27)
        alpha_to_nums = {nums[i]: alphabet[i] for i in range(len(alphabet))}

        print(alpha_to_nums)
        res = ''
        if columnNumber == 0:
            return -1
        for each in range(1,columnNumber):
            #print(alpha_to_nums[each])
            index = alpha_to_nums[each] if each < 26 else alpha_to_nums[ (26-columnNumber//26)]
            # print(index)
            #res += (alpha_to_nums[each] if each < 26 else alpha_to_nums[ (26-columnNumber//26)])
        return  res
print(chr(20))
print(ord('aa'))
#print(Solution().convertToTitle(28))



