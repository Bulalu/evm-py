
#stack of 256-bit words with a maximum size of 1024

class StackOverflow(Exception):
    """Overflowing bro"""

class StackUnderflow(Exception):
    """Underflow bro"""

class InvalidStackItem(Exception):
    """Invalid Stack item bro"""

class Stack:
    def __init__(self, max_depth=1024) -> None:
        self.stack = []
        self.max_depth = max_depth

    def push(self, item: int) -> None:
        if item < 0 or item > 2**256 -1:
            raise InvalidStackItem()

        if (len(self.stack) + 1) > self.max_depth:
            raise StackOverflow()

        self.stack.append(item)

    def pop(self) -> int:
        if (len(self.stack)) == 0:
            raise StackUnderflow()

        return self.stack.pop()

    def check(self) -> list:
        return self.stack

    
stack = Stack()
stack.push(23)
stack.push(34)
stack.push(90)
stack.pop()
print(stack.check())
