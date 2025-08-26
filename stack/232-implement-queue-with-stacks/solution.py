class MyQueue:

    def __init__(self):
        self.push_stk = []
        self.pop_stk = []    

    def push(self, x: int) -> None:
        self.push_stk.append(x)

    def pop(self) -> int:
        self.peek()
        return self.pop_stk.pop()

    def peek(self) -> int:
        if not self.pop_stk:
            while self.push_stk:
                self.pop_stk.append(self.push_stk.pop())

        return self.pop_stk[-1]

    def empty(self) -> bool:
        return len(self.push_stk) == 0 and len(self.pop_stk) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()