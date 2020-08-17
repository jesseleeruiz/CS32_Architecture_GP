# Let's build a data driven machine!

# What do we need to have our machine working?
"""
- Some sort of memory
- Some way of stopping operation
- Some way of keeping the CPU running
- Some sort of storage for local variables sperate from main RAM (memory) eg; Registers
- Some sort of operations that can be performed such as (printing something, saving data to a variable[register] )
- Some FETCH, DECODE, EXECUTE CYCLE

"""

# Operations that we can perform
PRINT_VLAD = 1
HALT = 2
PRINT_NUM = 3
PRINT_REG = 4
SAVE = 5
ADD = 6
SUB = 7
MULTI = 8

# some sort of memory
memory = [1, 4, 3, 5, 300, 3, 4, 3, 1, 1, 3, 120, 2]

# keep track of running?
running = True

# Need to keep track of where we are in memory
    # Some sort of counter
pc = 0

# Some local var holders [registers]
registers = [0] * 10

# Size of Opcode
op_size = 1

# REPL to run once per cycle of CPU
# inside this we will have our FETCH, DECODE, EXECUTE CYCLE
while running:
    # Fetch
    cmd = memory[pc]

    # Decode
    if cmd == PRINT_VLAD:
        # Execute
        print("Vlad")
        op_size = 1
    elif cmd == HALT:
        running = False
    elif cmd == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        op_size = 2
    elif cmd == PRINT_REG:
        index_of_reg = memory[pc + 1]
        num_at_reg = registers[index_of_reg]
        print(num_at_reg)
        op_size = 2
    elif cmd == SAVE:
        num_to_save = memory[pc + 1]
        reg_index = memory[pc + 2]
        registers[reg_index] = num_to_save
        op_size = 3
    elif cmd == ADD:
        reg_index_a = memory[pc + 1]
        reg_index_b = memory[pc + 2]
        registers[reg_index_a] += registers[reg_index_b]
        op_size = 3
    elif cmd == SUB:
        reg_index_a = memory[pc + 1]
        reg_index_b = memory[pc + 2]
        registers[reg_index_a] -= registers[reg_index_b]
        op_size = 3
    elif cmd == MULTI:
        reg_index_a = memory[pc + 1]
        reg_index_b = memory[pc + 2]
        registers[reg_index_a] *= registers[reg_index_b]
        op_size = 3

    pc += op_size