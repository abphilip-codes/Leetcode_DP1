# 91
# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        a, b = 1, 0
        for z in range(len(s)-1, -1, -1):
            k = s[z]
            if(k=="0"): a, b = 0, a
            elif(k=="1"): a, b = a + b, a
            elif(k=="2" and (z+1<len(s)) and (s[z+1]<"7")): a, b = a + b, a
            else: b = a
        return a