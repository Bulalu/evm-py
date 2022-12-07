
#stack of 256-bit words with a maximum size of 1024

class StackUnderflow(Exception):
    ...


class StackOverflow(Exception):
    ...


class InvalidStackItem(Exception):
    ...

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

    def __str__(self) -> str:
        return str(self.stack)

    def __repr__(self) -> str:
        return str(self)

    
stack = Stack()
stack.push(23)
stack.push(1)
stack.push(90)
stack.pop()
print(type(stack.__str__()))
print(type(stack.__repr__()))
