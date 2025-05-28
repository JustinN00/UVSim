
from UVSim.cpu import CPU

MEMORY_SIZE = 100

class UVSim:
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
                    
                    #check if line is a valid instruction
                    if False:
                        raise ValueError()


                    self.memory[i] = int(line)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            exit(1)
        except ValueError:
            print(f"Invalid instruction in file: {line}")
            exit(1)
    
    def run_program(self):
        self.load_program()
        cpu = CPU()


        



if __name__ == "__main__":

    sim = UVSim()
    sim.run_program()
