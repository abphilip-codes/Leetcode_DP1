# 279
# https://leetcode.com/problems/perfect-squares/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def f(word1, z, word2, y, c):
            if(z<0 or y<0): return z + 1 + y + 1
            if((z, y) in c): return c[(z, y)]

            if(word1[z]==word2[y]): result = f(word1, z-1, word2, y-1, c)
            else: result = min(f(word1, z-1, word2, y, c),
                               f(word1, z, word2, y-1, c),
                               f(word1, z-1, word2, y-1, c)) + 1
            c[(z, y)] = result
            return result
        return f(word1, len(word1)-1, word2, len(word2)-1, {})