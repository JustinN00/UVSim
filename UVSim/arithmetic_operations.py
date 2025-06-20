
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
        cpu.accumulator += value
    elif opcode == SUBTRACT:
        log_message = f"SUBTRACT value: {value} from accumulator: {cpu.accumulator}"
        cpu.accumulator -= value
    elif opcode == DIVIDE:
        log_message = f"DIVIDE accumulator: {cpu.accumulator} by value: {value}"
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        cpu.accumulator //= value
    elif opcode == MULTIPLY:
        log_message = f"MULTIPLY accumulator: {cpu.accumulator} by value: {value}"
        cpu.accumulator *= value
    else:
        raise ValueError("Invalid opcode.")
    
    if cpu.accumulator > 9999:
        cpu.accumulator -= 9999
    elif cpu.accumulator < -9999:
        cpu.accumulator += 9999
    return log_message
