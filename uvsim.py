
from UVSim.cpu import NewCPU
from UVSim.file_loader import FileLoader
from UVSim.memory import Memory
from UVSim.gui import UVSimGUI

class UVSim:
    @staticmethod
    def run_program():
        file_loader = FileLoader()
        memory = Memory()
        cpu = NewCPU(memory, file_loader)
        UVSimGUI(cpu)
        
if __name__ == "__main__":
    sim = UVSim()
    sim.run_program()