class Solution: 
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = []
        i = j = 0
        while i < n or j < m:
            if i < n:
                res.append(word1[i])
            if j < m:
                res.append(word2[j])
            i += 1
            j += 1
        return "".join(res)