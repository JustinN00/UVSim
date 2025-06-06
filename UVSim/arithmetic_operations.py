class SimpleProcessor:
    def __init__(self):
        self.accumulator = 0
        self.memory = [0] * 100  # Initialize memory with 100 words (all 0)
        self.opcodes = {
            30: self.add,
            31: self.subtract,
            32: self.divide,
            33: self.multiply
        }
    
    def load_accumulator(self, value):
        """Load a value into the accumulator"""
        self.accumulator = value
    
    def store_memory(self, address, value):
        """Store a value at a specific memory address"""
        if 0 <= address < len(self.memory):
            self.memory[address] = value
        else:
            raise IndexError("Memory address out of range")
    
    def add(self, address):
        """Add memory word to accumulator (opcode 30)"""
        self.accumulator += self.memory[address]
    
    def subtract(self, address):
        """Subtract memory word from accumulator (opcode 31)"""
        self.accumulator -= self.memory[address]
    
    def divide(self, address):
        """Divide accumulator by memory word (opcode 32)"""
        if self.memory[address] == 0:
            raise ZeroDivisionError("Attempt to divide by zero")
        self.accumulator //= self.memory[address]  # Using integer division
    
    def multiply(self, address):
        """Multiply accumulator by memory word (opcode 33)"""
        self.accumulator *= self.memory[address]
    
    def execute(self, opcode, address):
        """Execute the specified operation"""
        if opcode in self.opcodes:
            self.opcodes[opcode](address)
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

# Example usage
if __name__ == "__main__":
    processor = SimpleProcessor()
    
    # Initialize some memory locations
    processor.store_memory(10, 5)   # Memory location 10 = 5
    processor.store_memory(11, 3)   # Memory location 11 = 3
    processor.store_memory(12, 10)  # Memory location 12 = 10
    
    # Test operations
    processor.load_accumulator(20)
    processor.execute(30, 10)  # ADD: 20 + 5 = 25
    print("After ADD:", processor.accumulator)
    
    processor.execute(31, 11)  # SUBTRACT: 25 - 3 = 22
    print("After SUBTRACT:", processor.accumulator)
    
    processor.execute(33, 10)  # MULTIPLY: 22 * 5 = 110
    print("After MULTIPLY:", processor.accumulator)
    
    processor.execute(32, 12)  # DIVIDE: 110 / 10 = 11
    print("After DIVIDE:", processor.accumulator)
