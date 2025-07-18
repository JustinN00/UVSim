
from UVSim.arithmetic_operations import perform_operation
from UVSim.control_operations import branch, branchneg, branchzero, halt
from UVSim.io_operations import read, write
from UVSim.load_store_operations import load, store
from UVSim.memory import Memory
from UVSim.file_loader import FileLoader

operations = {
    "10": {"method": read, "args": ["user_input", "memory"]}, #READ
    "11": {"method": write, "args": ["memory"]}, #WRITE
    "20": {"method": load, "args": ["memory"]}, #LOAD
    "21": {"method": store, "args": ["memory"]}, #STORE
    "30": {"method": perform_operation, "args": ["op_code","memory"]}, #ADD
    "31": {"method": perform_operation, "args": ["op_code","memory"]}, #SUBTRACT
    "32": {"method": perform_operation, "args": ["op_code","memory"]}, #DIVIDE
    "33": {"method": perform_operation, "args": ["op_code","memory"]}, #MULTIPLY
    "40": {"method": branch, "args": ["memory"]}, #BRANCH
    "41": {"method": branchneg, "args": ["memory"]}, #BRANCHNEG
    "42": {"method": branchzero, "args": ["memory"]}, #BRANCHZERO
    "43": {"method": halt, "args": []}, #HALT
}

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
            instruction = str(self.memory.load(self.instruction_counter))
            op_code = instruction[-4:-2]
            argument = instruction[-2:]

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



