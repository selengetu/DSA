class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t = []
        for num in nums:
            if num != val:
                t.append(num)
        for i in range(len(t)):
            nums[i] = t[i]
        return len(t)