class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxS = 0
        l = 0
        charC = set()

        for r in range(len(s)):
            while s[r] in charC:
                charC.remove(s[l])
                l +=1
            charC.add(s[r])
            maxS = max(maxS, r-l+1)
        return maxS