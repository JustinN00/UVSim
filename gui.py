import tkinter as tk
from tkinter import filedialog
from UVSim.cpu import CPU


class UVSimGUI:
    def __init__(self, cpu: CPU):
        #Variables
        self.file_path = None
        self.cpu = cpu

        #Window setup
        self.window = tk.Tk()
        self.window.title("UVSim")
        self.window.geometry("600x400")

        #Widget setup
        self.file_label = tk.Label(self.window, text="No file selected", justify="left")
        self.file_button = tk.Button(self.window, text="Select File", command=self.select_file)
        self.run_button = tk.Button(self.window, text="Run Program", command=self.run_program)

        self.file_label.pack(pady=20)
        self.file_button.pack()
        self.run_button.pack()

        #Run
        self.window.mainloop()

    def select_file(self):
        """Prompt user to select a txt file"""
        file_path = filedialog.askopenfilename()
        if file_path:
            if ".txt"  in file_path:
                self.file_label.config(text=f"Selected: {file_path}", fg="black")
                self.file_path = file_path
            else:
                self.file_label.config(text="Must select a txt file", fg="red")
        
    def run_program(self):
        """Pass file path to cpu and run"""
        if self.file_path is None:
            return
        else:
            self.cpu.run_program(self.file_path)


if __name__ == "__main__":

    cpu = CPU()
    uvsim_gui = UVSimGUI(cpu)
