class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.stack1.append(x)
        else:
            for i in self.stack1[::-1]:
                self.stack2.append(i)

            self.stack1.clear()
            self.stack1.append(x)
            print(self.stack2)

            for i in self.stack2[::-1]:
                self.stack1.append(i)
            self.stack2.clear()
            print(self.stack1)
        

    def pop(self) -> int:
        e = self.stack1[-1]
        self.stack1.pop()
        return e
        

    def peek(self) -> int:
        return self.stack1[-1]
        

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()