import tkinter as tk
from tkinter import filedialog
from tkinter import END
from UVSim.cpu import NewCPU


class UVSimGUI:
    def __init__(self, cpu: NewCPU):
        #Variables
        self.file_path = None
        self.cpu = cpu

        #Window setup
        self.window = tk.Tk()
        self.window.title("UVSim")

        self.input_var = tk.StringVar()

        #Widget setup
        self.file_label = tk.Label(self.window, text="No file selected", justify="left", wraplength=150)
        self.file_button = tk.Button(self.window, text="Select File", command=self.select_file)
        self.run_button = tk.Button(self.window, text="Run Program", command=self.run_program)
        self.output = tk.Text(self.window)
        self.input = tk.Entry(self.window, textvariable=self.input_var)
        self.input.config(state="disabled")
        self.submit_button = tk.Button(self.window, text="Submit Input", command=self.submit_input)


        self.file_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.file_button.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.run_button.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.output.grid(row=0, column=1, rowspan=4, columnspan=2, padx=10, pady=5, sticky='nsew')
        self.input.grid(row=5, column=1, padx=10, pady=5, sticky='ew')
        self.submit_button.grid(row=5, column=2, padx=10, pady=5, sticky='w')

        
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
        self.output.delete(1.0, END)
        if self.file_path is None:
            return
        else:
            error = self.cpu.load_program(self.file_path)
            if error:
                self.output.insert(END, error)
                return
            while self.cpu.instruction_counter < 100:
                user_input = None
                if str(self.cpu.memory.load(self.cpu.instruction_counter))[-4:-2] == "10":
                    user_input = self.get_valid_input()

                output = self.cpu.run_next_command(user_input)
                if output is not None:
                    self.output.insert(END, output + "\n")

    def get_valid_input(self) -> int:
        self.input.config(state="normal")
        self.input_ready = tk.BooleanVar(value=False)
        self.output.insert(END, "READ: enter a value and click submit\n")
        self.window.wait_variable(self.input_ready)
        self.input.config(state="disabled")
        return self.user_input_value

    def submit_input(self):
        try:
            value = int(self.input_var.get())
            if -9999 <= value <= 9999:
                self.user_input_value = value
                self.input_var.set("")
                self.input.config(bg="white")
                self.input_ready.set(True)
                return value
            self.output.insert(END, "Error: Value must be between -9999 and 9999.\n")
            self.input.config(bg="red")
        except ValueError:
            self.output.insert(END, "Error: Invalid input. Please enter a signed integer.\n")
            self.input.config(bg="red")
