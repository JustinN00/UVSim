
# Define opcodes
ADD = 30
SUBTRACT = 31
DIVIDE = 32
MULTIPLY = 33

def perform_operation(cpu, opcode: int, address: int):
    value = cpu.memory.load(address)
    log_message = ""

    if opcode == ADD:
        log_message = f"ADD value: {value} to accumulator: {cpu.accumulator}"
        cpu.accumulator = int(cpu.accumulator) + int(value)
    elif opcode == SUBTRACT:
        log_message = f"SUBTRACT value: {value} from accumulator: {cpu.accumulator}"
        cpu.accumulator = int(cpu.accumulator) - int(value)
    elif opcode == DIVIDE:
        log_message = f"DIVIDE accumulator: {cpu.accumulator} by value: {value}"
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        cpu.accumulator = int(cpu.accumulator) // int(value)
    elif opcode == MULTIPLY:
        log_message = f"MULTIPLY accumulator: {cpu.accumulator} by value: {value}"
        cpu.accumulator = int(cpu.accumulator) * int(value)
    else:
        raise ValueError("Invalid opcode.")
    
    if int(cpu.accumulator) > 999999:
        cpu.accumulator = int(cpu.accumulator) - 999999
    elif int(cpu.accumulator) < -999999:
        cpu.accumulator = int(cpu.accumulator) + 999999
    return log_message
