
from UVSim.cpu import CPU

class UVSim:
    def run_program(filename: str):
        cpu = CPU()
        cpu.run_program(filename)


if __name__ == "__main__":
    sim = UVSim()
    sim.run_program()
