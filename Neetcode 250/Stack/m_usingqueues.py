class MyStack:

    def __init__(self):
        self.q = None

    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    def pop(self) -> int:
        top = self.q.popleft()
        self.q = self.q.popleft()
        return top

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q