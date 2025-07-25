
from UVSim.arithmetic_operations import perform_operation
from UVSim.control_operations import branch, branchneg, branchzero, halt
from UVSim.io_operations import read, write
from UVSim.load_store_operations import load, store
from UVSim.memory import Memory
from UVSim.file_loader import FileLoader
from enum import Enum

operations = {
    "010": {"method": read, "args": ["user_input", "memory"]}, #READ
    "011": {"method": write, "args": ["memory"]}, #WRITE
    "020": {"method": load, "args": ["memory"]}, #LOAD
    "021": {"method": store, "args": ["memory"]}, #STORE
    "030": {"method": perform_operation, "args": ["op_code","memory"]}, #ADD
    "031": {"method": perform_operation, "args": ["op_code","memory"]}, #SUBTRACT
    "032": {"method": perform_operation, "args": ["op_code","memory"]}, #DIVIDE
    "033": {"method": perform_operation, "args": ["op_code","memory"]}, #MULTIPLY
    "040": {"method": branch, "args": ["memory"]}, #BRANCH
    "041": {"method": branchneg, "args": ["memory"]}, #BRANCHNEG
    "042": {"method": branchzero, "args": ["memory"]}, #BRANCHZERO
    "043": {"method": halt, "args": []}, #HALT
}

class OpCodes(Enum):
    read = "010"
    write = "011"
    load = "020"
    store = "021"
    add = "030"
    subtract = "031"
    divide = "032"
    multiply = "033"
    branch = "040"
    branchneg = "041"
    branchzero = "042"
    halt = "043"

class NewCPU:
    def __init__(self, memory: Memory, file_loader: FileLoader):
        self.memory = memory
        self.file_loader = file_loader
        self.accumulator = 0
        self.instruction_counter = 0

    def load_program(self, filename: str) -> str | None:
        self.accumulator = 0
        self.instruction_counter = 0
        loaded_instructions, error = self.file_loader.load_file(filename)
        if error:
            return error
        self.memory.store_instructions(loaded_instructions)
        return None

    def run_next_command(self, user_input: str | None):
            instruction = self.memory.load(self.instruction_counter)

            for character in ["+","-"]:
                instruction = instruction.replace(character, "")

            #Convert instruction from legacy 4 length to new 6 length
            if len(instruction) == 4:

                if "0" + instruction [-4:2] in [code.value for code in OpCodes]:
                    instruction = "0" + instruction[-4:-2] + "0" + instruction [-2:]
                else:
                    instruction = ""

            op_code = instruction[-6:-3]
            argument = instruction[-3:]

            #Operation is a value and should be skipped
            if op_code not in [code.value for code in OpCodes]:
                output = None
            else:
                operation = operations[op_code]
                args = [self]
                for arg in operation["args"]:
                    match arg:
                        case "user_input": 
                            args.append(user_input)
                        case "memory": 
                            args.append(int(argument))
                        case "accumulator":
                            args.append(self.accumulator)
                        case "counter": 
                            args.append(self.instruction_counter)
                        case "op_code":
                            args.append(int(op_code))
                output = operation["method"](*args)

            self.instruction_counter += 1
            return output



