class Solution:
    def reverseString(self, s: List[str]) -> None:
        tmp = []
        for i in range(len(s) - 1, -1, -1):
            tmp.append(s[i])
        for j in range(len(s)):
            s[j] = tmp[j]
    

    def reverseString(self, s: List[str]) -> None:
        s.reverse()

        

