

def branch(cpu, location):
    print(f"BRANCH to {location}")
    cpu.instruction_counter = location - 1

def branchneg(cpu, location):
    if cpu.accumulator < 0:
        print(f"BRANCHNEG to {location}")
        cpu.instruction_counter = location -1

def branchzero(cpu, location):
    if cpu.accumulator == 0:
        print(f"BRANCHZERO to {location}")
        cpu.instruction_counter = location -1

def halt(cpu):
    print("HALT called")
    cpu.instruction_counter = 99

