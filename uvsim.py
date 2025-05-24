MEMORY_SIZE = 100

class UVSim:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE
        self.accumulator = 0
        self.instruction_counter = 0
        self.running = True

    def load_program(self, filename):
        try:
            with open(filename, 'r') as file:
                for i, line in enumerate(file):
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if i >= MEMORY_SIZE:
                        raise MemoryError("Program exceeds memory limit.")
                    self.memory[i] = int(line)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            exit(1)
        except ValueError:
            print(f"Invalid instruction in file: {line}")
            exit(1)


if __name__ == "__main__":
    main()
