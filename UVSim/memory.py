
class Memory:
    def __init__(self):
        self.memory = [""] * 250

    def load(self, address: int) -> int:
        if address < 0 or address > 249:
            raise ValueError(f"Attempted to access memory location {address}, which is out of range")
        return self.memory[address]
    
    def store(self, address: int, value: int) -> None:
        if address < 0 or address > 249:
            raise ValueError(f"Attempted to store in memory location {address}, which is out of range")
        str_value = str(value)
        needed_padding = 6 - len(str_value)
        int_sign = "+" if value >= 0 else "-"
        str_value = f"{int_sign}{'0' * needed_padding}{str_value}"

        self.memory[address] = str_value

    def store_instructions(self, instructions: list[int]) -> None:
        for i, instruction in enumerate(instructions):
            self.memory[i] = instruction

    def reset(self) -> None:
        self.memory = [""] * 250

    