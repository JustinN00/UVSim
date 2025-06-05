MEMORY_SIZE = 100




def temp_add(num1, num2):
    return num1 + num2

def temp(*args):
    pass



#TODO move method references to actual methods
operations = {
    "10": {"method": temp, "store": "memory", "args": ["memory"]}, #READ
    "11": {"method": temp, "store": None, "args": ["memory"]}, #WRITE
    "20": {"method": temp, "store": "accumulator", "args": ["memory"]}, #LOAD
    "21": {"method": temp, "store": "memory", "args": ["accumulator"]}, #STORE
    "30": {"method": temp_add, "store": "accumulator", "args": ["accumulator", "memory"]}, #ADD
    "31": {"method": temp, "store": "accumulator", "args": ["accumulator", "memory"]}, #SUBTRACT
    "32": {"method": temp, "store": "accumulator", "args": ["accumulator", "memory"]}, #DIVIDE
    "33": {"method": temp, "store": "accumulator", "args": ["accumulator", "memory"]}, #MULTIPLY
    "40": {"method": temp, "store": "counter", "args": ["memory"]}, #BRANCH
    "41": {"method": temp, "store": "counter", "args": ["accumulator", "counter"]}, #BRANCHNEG
    "42": {"method": temp, "store": "counter", "args": ["accumulator", "counter"]}, #BRANCHZERO
    "43": {"method": temp, "store": None, "args": []}, #HALT
}



class CPU:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE
        self.accumulator = 0
        self.instruction_counter = 0
        self.running = True

    def load_program(self, filename: str) -> None:
        """Load the commands from specified file into memory
        Args:
            filename: txt file location to load commands from
        """
        try:
            with open(filename, 'r') as file:
                for i, line in enumerate(file):
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if i >= MEMORY_SIZE:
                        raise MemoryError("Program exceeds memory limit.")
                    
                    #TODO check if line is a valid instruction
                    if False:
                        raise ValueError()


                    self.memory[i] = int(line)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            exit(1)
        except ValueError:
            print(f"Invalid instruction in file: {line}")
            exit(1)
    
    def run_program(self, filename: str):
        self.load_program(filename)
        while True:
             if self.instruction_counter == 100:
                 raise ValueError("CPU instruction counter has exceeded max memory...")
             instruction = str(self.memory[self.instruction_counter])
             op_code = instruction[-4:-2]
             argument = instruction[-2:]

             operation = operations[op_code]

             args = []
             for arg in operation["args"]:
                 match arg:
                     case "memory": 
                         args.append(int(argument))
                     case "accumulator":
                         args.append(self.accumulator)
                     case "counter": 
                         args.append(self.instruction_counter)

             value = operation["method"](*args)
             match operation["store"]:
                 case "accumulator":
                     self.accumulator = value
                 case "memory":
                     self.memory[args] = value
                 case "counter":
                     self.instruction_counter = value
             self.instruction_counter += 1

