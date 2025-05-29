MEMORY_SIZE = 100




def temp_add(num1, num2):
    return num1 + num2



operations = {
    "10": {"method": temp_add, "store": "accumulator"},
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
        self.load_program()
        while True:
             instruction = str(self.memory[self.instruction_counter])
             negative = True if "-" in instruction else False
             op_code = instruction[-4:-2]
             argument = instruction[-2:]

             operation = operations[op_code]
             args = [argument] if operations["args"] else []
             value = operation["method"](*args)
             match operation["store"]:
                 case "accumulator":
                     self.accumulator = value
                 case "memory":
                     self.memory[args] = value

             self.instruction_counter += 1
