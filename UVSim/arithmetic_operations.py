
# Define opcodes
ADD = 30
SUBTRACT = 31
DIVIDE = 32
MULTIPLY = 33

def perform_operation(cpu, opcode: int, address: int):
    if address < 0 or address >= len(cpu.memory):
        raise ValueError("Invalid memory address.")

    value = cpu.memory[address]

    if opcode == ADD:
        cpu.accumulator += value
    elif opcode == SUBTRACT:
        cpu.accumulator -= value
    elif opcode == DIVIDE:
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        cpu.accumulator //= value
    elif opcode == MULTIPLY:
        cpu.accumulator *= value
    else:
        raise ValueError("Invalid opcode.")
