
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
        print(f"ADD value: {value} to accumulator: {cpu.accumulator}")
        cpu.accumulator += value
    elif opcode == SUBTRACT:
        print(f"SUBTRACT value: {value} from accumulator: {cpu.accumulator}")
        cpu.accumulator -= value
    elif opcode == DIVIDE:
        print(f"DIVIDE accumulator: {cpu.accumulator} by value: {value}")
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        cpu.accumulator //= value
    elif opcode == MULTIPLY:
        print(f"MULTIPLY accumulator: {cpu.accumulator} by value: {value}")
        cpu.accumulator *= value
    else:
        raise ValueError("Invalid opcode.")
    
    print(f"New accumulator value: {cpu.accumulator}")
