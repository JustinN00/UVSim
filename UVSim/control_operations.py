

def branch(cpu, location):
    cpu.instruction_counter = location - 1
    return f"BRANCH to {location}"

def branchneg(cpu, location):
    if int(cpu.accumulator) < 0:
        cpu.instruction_counter = location -1
        return f"BRANCHNEG to {location}"

def branchzero(cpu, location):
    if int(cpu.accumulator) == 0:
        cpu.instruction_counter = location -1
        return f"BRANCHZERO to {location}"

def halt(cpu):
    cpu.instruction_counter = 99
    return "HALT called"

