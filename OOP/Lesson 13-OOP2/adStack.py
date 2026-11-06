
class Stack:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.items = []

    def isEmpty(self) -> bool:
        return len(self.items) == 0

    def isFull(self) -> bool:
        return len(self.items) == self.max_size

    def peek(self):
        if self.isEmpty():
            print("Cannot peek: Stack is empty.")
        return self.items[-1]

    def push(self, x) -> None:
        if self.isFull():
            print(f"Cannot push '{x}': Stack is full.")
        self.items.append(x)

    def pop(self):
        if self.isEmpty():
            print("Cannot pop: Stack is empty.")
        return self.items.pop()