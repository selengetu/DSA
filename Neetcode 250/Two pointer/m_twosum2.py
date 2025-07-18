class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)- 1
        while l < r:
            sumT = numbers[l] + numbers[r]
            print(sumT)
            if sumT > target:
                r = r-1
            elif sumT < target:
                l = l+1
            else:
                return [l+1, r+1]