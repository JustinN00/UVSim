# UVSim
UVSim software simulator CS2450


UVSim is a simple yet powerful virtual machine that interprets programs written in BasicML. It simulates a computer system with CPU, registers, and main memory, capable of executing fundamental arithmetic, I/O, and control operations.

System Architecture

How to run:

    To run the simulator, run the uvsim.py file in the command line
    example:   python uvsim.py

    Use the select file button to select a .txt file
    Then use the run program button to run your program
    If user input is required, enter it in the field next to the submit button, then click the button
    

UVSim consists of:

    250-word memory (locations 00-249)

    Accumulator register for calculations

    Program counter for instruction sequencing

    Instruction set with 13 operations

    Functionality to support multiple files simultaneously

BasicML Instruction Format

UV SIM  supports signed four-digit and signed six-digit number files.

    NOTE: All four-digit number files will be converted into six-digit number files by the program. Conversion is done by adding a 0 to both the front of the file and the front of the memory address. 
    
Instructions for a signed six-digit number:

    First 3 digits: 0 + Operation code

    Last 3 digits: Memory address operand

    Example: +030015 = ADD operation using memory location 15

    
Instruction Set
I/O Operations

    010 READ - Read from keyboard into memory

    011 WRITE - Write from memory to screen

Load/Store Operations

    020 LOAD - Memory → Accumulator

    021 STORE - Accumulator → Memory

Arithmetic Operations

    030 ADD - Memory + Accumulator → Accumulator

    031 SUBTRACT - Accumulator - Memory → Accumulator

    032 DIVIDE - Accumulator / Memory → Accumulator

    033 MULTIPLY - Accumulator * Memory → Accumulator

Control Operations

    040 BRANCH - Jump to address

    041 BRANCHNEG - Jump if accumulator negative

    042 BRANCHZERO - Jump if accumulator zero

    043 HALT - Stop execution


GUI Controls

The interface includes the following elements:

    'Open File': Load a .txt BasicML program

    'Save File' and 'Save As': Save the current program

    Program Editor: Edit each instruction by line, using the Code and Value fields
    
    Code Field: Represents the instruction opcode (e.g., READ, ADD, BRANCH) or its mnemonic (if assembly support is enabled).

    Value Field: Represents the operand (memory address or data) associated with the instruction.

    Add, Update, Delete: Modify instructions

    Cut, Copy, Paste: Rearrange or duplicate instructions

    'Run Program': Execute the program

    Output panel: displays messages, errors, and program output

    Input field: Accepts user input when prompted by READ instructions
    
    Submit button: Submit typed input





Example Usage

This sample program reads two numbers, adds them, and prints the result:

```
+1007
+1008
+2007
+3008
+2109
+1109
+4300
+0000
+0000
+0000
```

If the two inputs are 4 and 5, the expected ouput is 9.

![UVSim GUI Screenshot](./Screenshot.png)
