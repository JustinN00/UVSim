# UVSim
UVSim software simulator CS2450


UVSim is a simple yet powerful virtual machine that interprets programs written in BasicML (Basic Machine Language). It simulates a computer system with CPU, registers, and main memory, capable of executing fundamental arithmetic, I/O, and control operations.
System Architecture

UVSim consists of:

    100-word memory (locations 00-99)

    Accumulator register for calculations

    Program counter for instruction sequencing

    Instruction set with 13 operations

BasicML Instruction Format

Each instruction is a signed four-digit decimal number:

    First 2 digits: Operation code

    Last 2 digits: Memory address operand

    Example: +3015 = ADD operation using memory location 15

Instruction Set
I/O Operations

    10 READ - Read from keyboard into memory

    11 WRITE - Write from memory to screen

Load/Store Operations

    20 LOAD - Memory → Accumulator

    21 STORE - Accumulator → Memory

Arithmetic Operations

    30 ADD - Memory + Accumulator → Accumulator

    31 SUBTRACT - Accumulator - Memory → Accumulator

    32 DIVIDE - Accumulator / Memory → Accumulator

    33 MULTIPLY - Accumulator * Memory → Accumulator

Control Operations

    40 BRANCH - Jump to address

    41 BRANCHNEG - Jump if accumulator negative

    42 BRANCHZERO - Jump if accumulator zero

    43 HALT - Stop execution
