
from UVSim.cpu import CPU
import sys
import os

class UVSim:
    @staticmethod
    def run_program(filename: str):
        cpu = CPU()
        cpu.run_program(filename)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError(f"Provide the instruction file path as an argument.")
    instruction_file = sys.argv[1]
    if not os.path.isfile(instruction_file):
        raise FileNotFoundError(f"The file {instruction_file} was not found or is not a file.")

    sim = UVSim()
    print(sys.argv[1])
    sim.run_program(sys.argv[1])
