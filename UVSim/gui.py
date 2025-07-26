import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, simpledialog
from tkinter import END, ttk
from UVSim.cpu import NewCPU
import json
import os

class UVSimGUI:
    def __init__(self, cpu: NewCPU):
        # Variables
        self.file_list = [None]
        self.function_list_list = []
        self.file_path = None
        self.cpu = cpu
        self.copied_function = None
        self.uvu_primary = "#4C721D"  # UVU green
        self.uvu_secondary = "#808080"  # Gray
        self.current_primary = self.uvu_primary
        self.current_secondary = self.uvu_secondary

        # Window setup
        self.window = tk.Tk()
        self.window.title("UVSim")
        self.window.geometry("900x750")
        
        # Load saved color scheme
        self.load_color_scheme()
        
        # Configure styles
        self.configure_styles()

        # Create menu
        self.create_menu()

        # Main frame
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left panel - file and program controls
        self.left_panel = ttk.Frame(self.main_frame)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # Right panel - output and input
        self.right_panel = ttk.Frame(self.main_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # File controls        
        self.file_button = ttk.Button(self.left_panel, text="Open File", command=self.select_file)
        self.file_button.pack(pady=5, fill=tk.X)
        
        self.save_button = ttk.Button(self.left_panel, text="Save File", command=self.save_file)
        self.save_button.pack(pady=5, fill=tk.X)
        
        self.save_as_button = ttk.Button(self.left_panel, text="Save As", command=self.save_file_as)
        self.save_as_button.pack(pady=5, fill=tk.X)

        # Program editor
        self.editor_label = ttk.Label(self.left_panel, text="Program Editor")
        self.editor_label.pack(anchor='w')
        
        close_button_frame = ttk.Frame(self.left_panel)
        close_button_frame.pack(fill=tk.X)

        self.close_tab_button = ttk.Button(close_button_frame, text="Close Active Tab", command=self.close_active_tab)
        self.close_tab_button.pack(side="right")

        self.style = ttk.Style()
        self.style.configure('TNotebook', tabposition = 'nw')
        self.notebook = ttk.Notebook(self.left_panel)
#        self.notebook.pack(fill=tk.X, pady=5)
        self.notebook.pack(expand=True, fill='both')
        
        self.create_tab()

        # Editor controls
        self.edit_controls = ttk.Frame(self.left_panel)
        self.edit_controls.pack(fill=tk.X, pady=5)
        
        self.code_label = ttk.Label(self.edit_controls, text="Code:")
        self.code_label.grid(row=0, column=0, sticky='w')
        self.code_entry = ttk.Entry(self.edit_controls)
        self.code_entry.grid(row=0, column=1, sticky='ew')
        
        self.value_label = ttk.Label(self.edit_controls, text="Value:")
        self.value_label.grid(row=1, column=0, sticky='w')
        self.value_entry = ttk.Entry(self.edit_controls)
        self.value_entry.grid(row=1, column=1, sticky='ew')
        
        self.edit_controls.grid_columnconfigure(1, weight=1)
        
        # Editor buttons
        self.button_frame = ttk.Frame(self.left_panel)
        self.button_frame.pack(fill=tk.X, pady=5)
        
        self.add_button = ttk.Button(self.button_frame, text="Add", command=self.add_function)
        self.add_button.grid(row=0, column=0, padx=2)
        
        self.update_button = ttk.Button(self.button_frame, text="Update", command=self.update_function)
        self.update_button.grid(row=0, column=1, padx=2)
        
        self.delete_button = ttk.Button(self.button_frame, text="Delete", command=self.delete_function)
        self.delete_button.grid(row=0, column=2, padx=2)
        
        self.move_up_button = ttk.Button(self.button_frame, text="↑", width=2, command=self.move_function_up)
        self.move_up_button.grid(row=1, column=0, padx=2)
        
        self.move_down_button = ttk.Button(self.button_frame, text="↓", width=2, command=self.move_function_down)
        self.move_down_button.grid(row=1, column=1, padx=2)
        
        self.cut_button = ttk.Button(self.button_frame, text="Cut", command=self.cut_function)
        self.cut_button.grid(row=1, column=2, padx=2)
        
        self.copy_button = ttk.Button(self.button_frame, text="Copy", command=self.copy_function)
        self.copy_button.grid(row=1, column=0, padx=2)
        
        self.paste_button = ttk.Button(self.button_frame, text="Paste", command=self.paste_function)
        self.paste_button.grid(row=1, column=1, padx=2)
        
        # Execution controls
        self.run_button = ttk.Button(self.left_panel, text="Run Program", command=self.run_program)
        self.run_button.pack(pady=10, fill=tk.X)

        # Color change buttons
        self.color_button_frame = ttk.Frame(self.left_panel)
        self.color_button_frame.pack(fill=tk.X, pady=5)

        self.primary_color_btn = ttk.Button(self.color_button_frame, text="Color of Scheme", command=lambda: self.change_single_color('primary'))
        self.primary_color_btn.pack(side=tk.LEFT, padx=2, expand=True)

        self.secondary_color_btn = ttk.Button(self.color_button_frame, text="Color of Texts", command=lambda: self.change_single_color('secondary'))
        self.secondary_color_btn.pack(side=tk.LEFT, padx=2, expand=True)

        self.button_color_btn = ttk.Button(self.color_button_frame, text="Color of Buttons", command=self.change_button_color)
        self.button_color_btn.pack(side=tk.LEFT, padx=2, expand=True)

        # Bind window close event to reset colors
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Output area
        self.output_frame = ttk.Frame(self.right_panel)
        self.output_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_label = ttk.Label(self.output_frame, text="Output")
        self.output_label.pack(anchor='w')
        
        self.output = tk.Text(self.output_frame, wrap=tk.WORD)
        self.output.pack(fill=tk.BOTH, expand=True)
        
        output_scroll = ttk.Scrollbar(self.output_frame, orient=tk.VERTICAL, command=self.output.yview)
        output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.output.config(yscrollcommand=output_scroll.set)

        # Input area
        self.input_frame = ttk.Frame(self.right_panel)
        self.input_frame.pack(fill=tk.X, pady=5)
        
        self.input_label = ttk.Label(self.input_frame, text="Input:")
        self.input_label.pack(side=tk.LEFT, padx=5)
        
        self.input_var = tk.StringVar()
        self.input_ready = tk.BooleanVar()
        self.input_ready.set(False)
        self.input = ttk.Entry(self.input_frame, textvariable=self.input_var)
        self.input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.input.config(state="disabled")
        
        self.submit_button = ttk.Button(self.input_frame, text="Submit", command=self.submit_input)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        # Apply color scheme
        self.apply_color_scheme()
        
        # Run
        self.window.mainloop()

    def create_menu(self):
        menubar = tk.Menu(self.window)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.select_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut_function)
        edit_menu.add_command(label="Copy", command=self.copy_function)
        edit_menu.add_command(label="Paste", command=self.paste_function)
        edit_menu.add_command(label="Delete", command=self.delete_function)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        # Settings menu
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Change Color Scheme", command=self.change_color_scheme)
        settings_menu.add_command(label="Reset to UVU Colors", command=self.reset_color_scheme)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        
        self.window.config(menu=menubar)

    def configure_styles(self):
        style = ttk.Style()
        style.configure('TButton', padding=5, foreground='black')  # Changed foreground to black
        style.configure('TEntry', padding=5)
        style.configure('TLabel', padding=5)
        style.configure('TFrame', padding=5)


    def change_single_color(self, color_type):
    #Change either primary or secondary color
        current_color = self.current_primary if color_type == 'primary' else self.current_secondary
        new_color = colorchooser.askcolor(title=f"Choose {color_type} color", initialcolor=current_color)[1]
        if new_color:
            if color_type == 'primary':
                self.current_primary = new_color
            else:
                self.current_secondary = new_color
            self.save_color_scheme()
            self.apply_color_scheme()

    def change_button_color(self):
    #Change the button foreground color
        style = ttk.Style()
        current_color = style.lookup('TButton', 'foreground')
        new_color = colorchooser.askcolor(title="Choose button text color", initialcolor=current_color)[1]
        if new_color:
            style.configure('TButton', foreground=new_color)
            style.map('TButton', foreground=[('active', new_color)])

    def on_close(self):
    #Reset colors and close the window
        # Reset to default colors
        self.current_primary = self.uvu_primary
        self.current_secondary = self.uvu_secondary
        style = ttk.Style()
        style.configure('TButton', foreground='black')
        style.map('TButton', foreground=[('active', 'black')])
        
        # Save and close
        self.save_color_scheme()
        self.window.destroy()

    def load_color_scheme(self):
        try:
            with open('uvsim_colors.json', 'r') as f:
                colors = json.load(f)
                self.current_primary = colors.get('primary', self.uvu_primary)
                self.current_secondary = colors.get('secondary', self.uvu_secondary)
        except (FileNotFoundError, json.JSONDecodeError):
            self.current_primary = self.uvu_primary
            self.current_secondary = self.uvu_secondary

    def save_color_scheme(self):
        colors = {
            'primary': self.current_primary,
            'secondary': self.current_secondary
        }
        with open('uvsim_colors.json', 'w') as f:
            json.dump(colors, f)
            
    def apply_color_scheme(self):
        # Apply colors to widgets
        self.window.configure(bg=self.current_primary)
        
        # Style configuration
        style = ttk.Style()
        style.configure('TFrame', background=self.current_primary)
        style.configure('TLabel', background=self.current_primary, foreground=self.current_secondary)
        style.configure('TButton', 
                    background=self.current_primary, 
                    foreground='black',  # Changed to black
                    bordercolor=self.current_primary,
                    darkcolor=self.current_primary,
                    lightcolor=self.current_primary)
        style.map('TButton',
                background=[('active', self.current_primary)],
                foreground=[('active', 'black')])  # Keep black when active
        style.configure('TEntry', fieldbackground='white', foreground='black')
        
        # Special widget configurations
        self.function_list.configure(
            bg='white',
            fg='black',
            selectbackground=self.current_primary,
            selectforeground=self.current_secondary
        )
        
        self.output.configure(
            bg='white',
            fg='black',
            insertbackground='black',
            selectbackground=self.current_primary,
            selectforeground=self.current_secondary
        )
        
        # Special widget configurations
        self.function_list.configure(
            bg='white',
            fg='black',
            selectbackground=self.current_primary,
            selectforeground=self.current_secondary
        )
        
        self.output.configure(
            bg='white',
            fg='black',
            insertbackground='black',
            selectbackground=self.current_primary,
            selectforeground=self.current_secondary
        )

    def change_color_scheme(self):
        primary = colorchooser.askcolor(title="Choose primary color", initialcolor=self.current_primary)[1]
        if primary:
            secondary = colorchooser.askcolor(title="Choose secondary color", initialcolor=self.current_secondary)[1]
            if secondary:
                self.current_primary = primary
                self.current_secondary = secondary
                self.save_color_scheme()
                self.apply_color_scheme()

    def reset_color_scheme(self):
        self.current_primary = self.uvu_primary
        self.current_secondary = self.uvu_secondary
        self.save_color_scheme()
        self.apply_color_scheme()


    def create_tab(self):
        self.editor_frame = ttk.Frame(self.notebook)
        self.editor_frame.pack(fill=tk.X, pady=5)
        tab_name = 'No file' if self.file_path is None else os.path.basename(self.file_path)
        self.notebook.add(self.editor_frame, text = tab_name)

        self.function_list = tk.Listbox(self.editor_frame, height=15, width=30)
        self.function_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.editor_frame, orient=tk.VERTICAL, command=self.function_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.function_list.config(yscrollcommand=scrollbar.set)
        self.function_list.bind('<<ListboxSelect>>', self.on_function_select)
        self.function_list_list.append(self.function_list)

        self.notebook.select(self.editor_frame)


    def close_active_tab(self):
        index = self.notebook.index('current')
        del self.file_list[index]
        del self.function_list_list[index]
        self.notebook.forget(index)


    def select_file(self):
        """Prompt user to select a txt file"""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    # Read and parse the file
                    lines = [line.strip() for line in f.readlines() if line.strip()]
                    
                    # Keep track of file
                    self.file_list.append(file_path)
                    self.file_path = file_path

                    self.create_tab()

                    # Add to listbox
                    for i, line in enumerate(lines):
                        self.function_list.insert(tk.END, f"{i:02d}: {line}")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def save_file(self):
        if not self.file_path:
            self.save_file_as()
            return
        
        try:
            with open(self.file_path, 'w') as f:
                # Get all functions from the listbox
                functions = []
                for i in range(self.function_list.size()):
                    item = self.function_list.get(i)
                    # Extract just the instruction part (after ": ")
                    instruction = item.split(": ", 1)[1] if ": " in item else item
                    functions.append(instruction + "\n")
                
                f.writelines(functions)
                messagebox.showinfo("Success", "File saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialdir=os.path.dirname(self.file_path) if self.file_path else None
        )
        
        if file_path:
            self.file_path = file_path
            self.save_file()

    def on_function_select(self, event):
        selected = self.function_list.curselection()
        if selected:
            item = self.function_list.get(selected[0])
            parts = item.split(": ", 1)[1].split() if ": " in item else item.split()
            if len(parts) >= 1:
                self.code_entry.delete(0, tk.END)
                self.code_entry.insert(0, parts[0])
            if len(parts) >= 2:
                self.value_entry.delete(0, tk.END)
                self.value_entry.insert(0, " ".join(parts[1:]))

    def add_function(self):
        if self.function_list.size() >= 250:
            messagebox.showwarning("Limit Reached", "Maximum of 250 functions allowed.")
            return
            
        code = self.code_entry.get().strip()
        value = self.value_entry.get().strip()
        
        if code:
            new_item = f"{self.function_list.size():02d}: {code}"
            if value:
                new_item += f" {value}"
            self.function_list.insert(tk.END, new_item)
            self.code_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)

    def update_function(self):
        selected = self.function_list.curselection()
        if selected:
            index = selected[0]
            code = self.code_entry.get().strip()
            value = self.value_entry.get().strip()
            
            if code:
                updated_item = f"{index:02d}: {code}"
                if value:
                    updated_item += f" {value}"
                self.function_list.delete(index)
                self.function_list.insert(index, updated_item)

    def move_function_up(self):
        selected = self.function_list.curselection()
        if selected and selected[0] > 0:
            index = selected[0]
            item = self.function_list.get(index)
            self.function_list.delete(index)
            self.function_list.insert(index-1, item)
            self.function_list.selection_set(index-1)

    def move_function_down(self):
        selected = self.function_list.curselection()
        if selected and selected[0] < self.function_list.size()-1:
            index = selected[0]
            item = self.function_list.get(index)
            self.function_list.delete(index)
            self.function_list.insert(index+1, item)
            self.function_list.selection_set(index+1)

    def cut_function(self):
        self.copy_function()
        self.delete_function()

    def copy_function(self):
        selected = self.function_list.curselection()
        if selected:
            self.copied_function = self.function_list.get(selected[0])

    def paste_function(self):
        if self.copied_function and self.function_list.size() < 100:
            # Remove the index part from the copied function
            parts = self.copied_function.split(": ", 1)
            new_item = f"{self.function_list.size():02d}: {parts[1]}" if len(parts) > 1 else self.copied_function
            self.function_list.insert(tk.END, new_item)
        elif self.function_list.size() >= 100:
            messagebox.showwarning("Limit Reached", "Maximum of 100 functions allowed.")

    def delete_function(self):
        selected = self.function_list.curselection()
        if selected:
            index = selected[0]
            self.function_list.delete(index)
            
            # Renumber remaining items
            for i in range(index, self.function_list.size()):
                item = self.function_list.get(i)
                parts = item.split(": ", 1)
                if len(parts) > 1:
                    self.function_list.delete(i)
                    self.function_list.insert(i, f"{i:02d}: {parts[1]}")

    def run_program(self):
        """Pass file path to cpu and run"""
        self.output.delete(1.0, END)

        self.function_list = self.function_list_list[self.notebook.index('current')]
        
        # Create a temporary file with current functions
        temp_file = "temp_program.txt"
        try:
            with open(temp_file, 'w') as f:
                for i in range(self.function_list.size()):
                    item = self.function_list.get(i)
                    instruction = item.split(": ", 1)[1] if ": " in item else item
                    f.write(instruction + "\n")
            
            error = self.cpu.load_program(temp_file)
            if error:
                self.output.insert(END, error)
                return
            
            while self.cpu.instruction_counter < 250:
                user_input = None
                next_instruction = self.cpu.memory.load(self.cpu.instruction_counter)
                for character in ["+","-"]:
                    next_instruction = next_instruction.replace(character, "")
                if len(next_instruction) == 4:
                    next_instruction = "0" + next_instruction + "0"
                if next_instruction[-6:-3] == "010":
                    user_input = self.get_valid_input()

                output = self.cpu.run_next_command(user_input)
                if output is not None:
                    self.output.insert(END, output + "\n")
                    self.output.see(END)  # Auto-scroll to bottom
        finally:
            # Clean up temporary file
            try:
                os.remove(temp_file)
            except:
                pass

    def get_valid_input(self) -> int:
        self.input_ready.set(False)
        self.input.config(state="normal")
        self.output.insert(END, "READ: enter a value and click submit\n")
        self.output.see(END)
        self.window.wait_variable(self.input_ready)
        self.input.config(state="disabled")
        return self.user_input_value

    def submit_input(self):
        try:
            value = int(self.input_var.get())
            if -999999 <= value <= 999999:
                self.user_input_value = value
                self.input_var.set("")
                self.input_ready.set(True)
                return value
            self.output.insert(END, "Error: Value must be between -9999 and 9999.\n")
        except ValueError:
            self.output.insert(END, "Error: Invalid input. Please enter a signed integer.\n")
            self.input.config(bg="red")
