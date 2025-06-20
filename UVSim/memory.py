
class Memory:
    def __init__(self):
        self.memory = [0] * 100

    def load(self, address: int) -> int:
        if address < 0 or address > 99:
            raise ValueError(f"Attempted to access memory location {address}, which is out of range")
        return self.memory[address]
    
    def store(self, address: int, value: int) -> None:
        if address < 0 or address > 99:
            raise ValueError(f"Attempted to store in memory location {address}, which is out of range")
        self.memory[address] = value

    def store_instructions(self, instructions: list[int]) -> None:
        for i, instruction in enumerate(instructions):
            self.memory[i] = instruction

    def reset(self) -> None:
        self.memory = [0] * 100

    