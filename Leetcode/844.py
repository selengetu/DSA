class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        for i in s:
            if i == '#':
                if len(list1) > 0:
                    list1.pop()
            else:
                list1.append(i)
       
        for n in t:
            if n == '#':
                if len(list2) > 0:
                    list2.pop()
            else:
                list2.append(n)
        

        return list1 == list2