# from .constants import MAX_UINT256, MAX_UINT8

MAX_UINT256 = 2 ** 256 - 1
MAX_UINT8 = 2 ** 8 - 1
MAX_STACK_DEPTH = 1024

class Memory:
    def __init__(self) -> None:
        self.memory = []

    def store(self, offset: int, value: int) -> None:
        if offset  < 0 or offset >  MAX_UINT256:
            raise InvalidMemoryAccess({"offset": offset, "value": value})

        if value < 0 or value > MAX_UINT8:
            raise InvalidMemoryValue({"offset": offset, "value": value})

        if offset >= len(self.memory):
            self.memory.extend([0] * (offset - len(self.memory) + 1))

        self.memory[offset] = value

    def load(self, offset:int):
        if offset < 0:
            raise InvalidMemoryAccess({"offset": offset})

        if offset >= len(self.memory):
            return 0

        return self.memory[offset]

    def load_range(self, offset: int, length: int) -> bytes:
        if offset < 0:
            raise InvalidMemoryAccess({"offset": offset, "length": length})

        return bytes(self.load(x) for x in range(offset, offset + length))




    def __str__(self) -> str:
        return str(self.memory)

    def __repr__(self) -> str:
        return str(self)


memory = Memory()
memory.store(4, 13)
print(memory.__str__())
print(memory.load(4))
print(memory.load_range(4, 4))




class InvalidMemoryAccess(Exception):
    ...


class InvalidMemoryValue(Exception):
    ...