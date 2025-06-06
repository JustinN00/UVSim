# control_operations.py

BRANCH = 40
BRANCHNEG = 41
BRANCHZERO = 42
HALT = 43

memory = [0] * 100
accumulator = 0
instruction_pointer = 0
halted = False

def load_instruction(address, instruction):
    if 0 <= address < len(memory):
        memory[address] = instruction
    else:
        raise ValueError("Invalid memory address")

def set_accumulator(value):
    global accumulator
    accumulator = value

def get_accumulator():
    return accumulator

def get_instruction_pointer():
    return instruction_pointer

def is_halted():
    return halted

def execute_instruction():
    global instruction_pointer, accumulator, halted

    if instruction_pointer < 0 or instruction_pointer >= len(memory):
        raise ValueError("Instruction pointer out of bounds")

    instruction = memory[instruction_pointer]
    opcode = instruction // 100
    operand = instruction % 100

    if opcode == BRANCH:
        instruction_pointer = operand
    elif opcode == BRANCHNEG:
        if accumulator < 0:
            instruction_pointer = operand
        else:
            instruction_pointer += 1
    elif opcode == BRANCHZERO:
        if accumulator == 0:
            instruction_pointer = operand
        else:
            instruction_pointer += 1
    elif opcode == HALT:
        halted = True
    else:
        raise ValueError(f"Invalid control opcode: {opcode}")

