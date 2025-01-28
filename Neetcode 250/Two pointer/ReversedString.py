class Solution:
    def reverseString(self, s: List[str]) -> None:
        tmp = []
        for i in range(len(s) - 1, -1, -1):
            tmp.append(s[i])
        for j in range(len(s)):
            s[j] = tmp[j]
    

    def reverseString(self, s: List[str]) -> None:
        s.reverse()

     
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1   

