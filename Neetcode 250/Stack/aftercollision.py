class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    a = 0
                    stack.pop()
                else:
                    a = 0
            if a:
                stack.append(a)
        return stack