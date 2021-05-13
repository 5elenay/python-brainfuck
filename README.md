# py-brainf*ck
Just a basic compiled that compiles your brainf*ck codes and gives you informations about memory, used cells, dumped version, logs etc...

**Note**: This compiler still have some bugs. If you wan't to fix, you just can fork & pull request

# Config
Check config.json first, quick information about config.json;
```js
{
    "MEM": 20, // MEM is the total cells for our brainfuck program.
    "DUMP_FILE": "./result/dump.py", // The dump file that will write when program finished and got some informations about the code. 
    "COMPILE_FILE": "./result/compiled.py", // The file that will write when brainfuck code turned into python code.
    "LOG_FILE": "./result/logs.txt", // Log file for our program actions.
    "DEBUG": true // Allow debug mode for compiler, will log everything to console.
}
```

# Usage
Simple Usage;
`python compiler.py ./example/fibonacci.bf`

Output: `... 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...`

Lets check the `./result/dump.py`;
```py
# DUMP RESULT | 13/05/2021 16:59:13
# =======================================================
# TOTAL CELL GIVEN: 20
# TOTAL CELL USED: 4
# TOTAL BYTE USED: 309
# MEMORY DUMP: [
    # CELL_0 -> 0 BYTE
    # CELL_1 -> 144 BYTE
    # CELL_2 -> 89 BYTE
    # CELL_3 -> 0 BYTE
    # CELL_4 -> 0 BYTE
    # CELL_5 -> 44 BYTE
    # CELL_6 -> 32 BYTE
    # CELL_7 -> 0 BYTE
    # CELL_8 -> 0 BYTE
    # CELL_9 -> 0 BYTE
    # CELL_10 -> 0 BYTE
    # CELL_11 -> 0 BYTE
    # CELL_12 -> 0 BYTE
    # CELL_13 -> 0 BYTE
    # CELL_14 -> 0 BYTE
    # CELL_15 -> 0 BYTE
    # CELL_16 -> 0 BYTE
    # CELL_17 -> 0 BYTE
    # CELL_18 -> 0 BYTE
    # CELL_19 -> 0 BYTE
# ]

# MINIFIED VERSION: [
    # LINE_1 -> +++++++++++>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++
    # LINE_2 -> ++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[
    # LINE_3 -> -<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[
    # LINE_4 -> <<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++
    # LINE_5 -> ++++++++++++++.[-]]++++++++++<[->-<]>+++++++++++++++++++++++++++++++++++++++++++
    # LINE_6 -> +++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>
    # LINE_7 -> >[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]
# ]
# =======================================================

import sys
memory, current, indent, compiled = [0 for byte in range(20)], 0, 0, ""

def change_byte(c, t, i = 1):
    if t == "+":
        if memory[c] + i <= 256:
            memory[c] += i
        else:
            memory[c] =  i % 255
    elif t == "-":
        if memory[c] - i >= 0:
            memory[c] -= i
        else:
            memory[c] = 256 - (i % 255)

change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
current = current + 1 if current < len(memory) - 1 else 0
change_byte(current, '+')
current = current + 1 if current < len(memory) - 1 else 0
current = current + 1 if current < len(memory) - 1 else 0
current = current + 1 if current < len(memory) - 1 else 0
current = current + 1 if current < len(memory) - 1 else 0
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
current = current + 1 if current < len(memory) - 1 else 0
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
change_byte(current, '+')
current = current - 1 if current > 0 else len(memory) - 1
current = current - 1 if current > 0 else len(memory) - 1
current = current - 1 if current > 0 else len(memory) - 1
current = current - 1 if current > 0 else len(memory) - 1
current = current - 1 if current > 0 else len(memory) - 1
current = current - 1 if current > 0 else len(memory) - 1

while memory[current] != 0:
    current = current + 1 if current < len(memory) - 1 else 0

    while memory[current] != 0:
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '+')
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '+')
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        change_byte(current, '-')

    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0

    while memory[current] != 0:
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        change_byte(current, '+')
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '-')

    current = current - 1 if current > 0 else len(memory) - 1

    while memory[current] != 0:
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')

        while memory[current] != 0:
            change_byte(current, '-')
            current = current - 1 if current > 0 else len(memory) - 1
            change_byte(current, '-')

            while memory[current] != 0:
                current = current + 1 if current < len(memory) - 1 else 0
                current = current + 1 if current < len(memory) - 1 else 0
                change_byte(current, '+')
                current = current + 1 if current < len(memory) - 1 else 0
                change_byte(current, '+')
                current = current - 1 if current > 0 else len(memory) - 1
                current = current - 1 if current > 0 else len(memory) - 1
                current = current - 1 if current > 0 else len(memory) - 1
                change_byte(current, '-')

            current = current + 1 if current < len(memory) - 1 else 0
            current = current + 1 if current < len(memory) - 1 else 0
            current = current + 1 if current < len(memory) - 1 else 0

            while memory[current] != 0:
                current = current - 1 if current > 0 else len(memory) - 1
                current = current - 1 if current > 0 else len(memory) - 1
                current = current - 1 if current > 0 else len(memory) - 1
                change_byte(current, '+')
                current = current + 1 if current < len(memory) - 1 else 0
                current = current + 1 if current < len(memory) - 1 else 0
                current = current + 1 if current < len(memory) - 1 else 0
                change_byte(current, '-')

            change_byte(current, '+')
            current = current - 1 if current > 0 else len(memory) - 1

            while memory[current] != 0:
                current = current + 1 if current < len(memory) - 1 else 0

                while memory[current] != 0:
                    change_byte(current, '-')

                current = current - 1 if current > 0 else len(memory) - 1

                while memory[current] != 0:
                    change_byte(current, '-')


            current = current + 1 if current < len(memory) - 1 else 0

            while memory[current] != 0:
                current = current - 1 if current > 0 else len(memory) - 1
                current = current - 1 if current > 0 else len(memory) - 1

                while memory[current] != 0:
                    current = current + 1 if current < len(memory) - 1 else 0
                    current = current + 1 if current < len(memory) - 1 else 0
                    current = current + 1 if current < len(memory) - 1 else 0
                    change_byte(current, '+')
                    current = current - 1 if current > 0 else len(memory) - 1
                    current = current - 1 if current > 0 else len(memory) - 1
                    current = current - 1 if current > 0 else len(memory) - 1
                    change_byte(current, '-')

                current = current + 1 if current < len(memory) - 1 else 0
                current = current + 1 if current < len(memory) - 1 else 0

                while memory[current] != 0:
                    change_byte(current, '-')


            current = current - 1 if current > 0 else len(memory) - 1
            current = current - 1 if current > 0 else len(memory) - 1

        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0

        while memory[current] != 0:
            current = current + 1 if current < len(memory) - 1 else 0
            current = current + 1 if current < len(memory) - 1 else 0
            change_byte(current, '+')
            current = current + 1 if current < len(memory) - 1 else 0
            change_byte(current, '+')
            current = current - 1 if current > 0 else len(memory) - 1
            current = current - 1 if current > 0 else len(memory) - 1
            current = current - 1 if current > 0 else len(memory) - 1
            change_byte(current, '-')

        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0

        while memory[current] != 0:
            current = current - 1 if current > 0 else len(memory) - 1
            current = current - 1 if current > 0 else len(memory) - 1
            current = current - 1 if current > 0 else len(memory) - 1
            change_byte(current, '+')
            current = current + 1 if current < len(memory) - 1 else 0
            current = current + 1 if current < len(memory) - 1 else 0
            current = current + 1 if current < len(memory) - 1 else 0
            change_byte(current, '-')

        change_byte(current, '+')
        current = current - 1 if current > 0 else len(memory) - 1

        while memory[current] != 0:
            current = current + 1 if current < len(memory) - 1 else 0

            while memory[current] != 0:
                change_byte(current, '-')

            current = current - 1 if current > 0 else len(memory) - 1

            while memory[current] != 0:
                change_byte(current, '-')


        current = current + 1 if current < len(memory) - 1 else 0

        while memory[current] != 0:
            current = current - 1 if current > 0 else len(memory) - 1
            current = current - 1 if current > 0 else len(memory) - 1
            change_byte(current, '+')
            current = current + 1 if current < len(memory) - 1 else 0
            current = current + 1 if current < len(memory) - 1 else 0

            while memory[current] != 0:
                change_byte(current, '-')


        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1

    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0

    while memory[current] != 0:
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        change_byte(current, '+')
        sys.stdout.write(chr(memory[current]))

        while memory[current] != 0:
            change_byte(current, '-')


    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    current = current - 1 if current > 0 else len(memory) - 1

    while memory[current] != 0:
        change_byte(current, '-')
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '-')
        current = current - 1 if current > 0 else len(memory) - 1

    current = current + 1 if current < len(memory) - 1 else 0
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    change_byte(current, '+')
    sys.stdout.write(chr(memory[current]))

    while memory[current] != 0:
        change_byte(current, '-')

    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1

    while memory[current] != 0:
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '+')
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '+')
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        change_byte(current, '-')

    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0

    while memory[current] != 0:
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        change_byte(current, '+')
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '-')

    current = current - 1 if current > 0 else len(memory) - 1
    change_byte(current, '-')

    while memory[current] != 0:
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        sys.stdout.write(chr(memory[current]))
        current = current + 1 if current < len(memory) - 1 else 0
        sys.stdout.write(chr(memory[current]))
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1

        while memory[current] != 0:
            change_byte(current, '-')


    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1

    while memory[current] != 0:
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '+')
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '+')
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        change_byte(current, '-')

    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0
    current = current + 1 if current < len(memory) - 1 else 0

    while memory[current] != 0:
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        current = current - 1 if current > 0 else len(memory) - 1
        change_byte(current, '+')
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '-')

    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1

    while memory[current] != 0:
        current = current - 1 if current > 0 else len(memory) - 1
        change_byte(current, '+')
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '-')

    current = current + 1 if current < len(memory) - 1 else 0

    while memory[current] != 0:
        current = current - 1 if current > 0 else len(memory) - 1
        change_byte(current, '+')
        current = current + 1 if current < len(memory) - 1 else 0
        change_byte(current, '-')

    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    current = current - 1 if current > 0 else len(memory) - 1
    change_byte(current, '-')
```
Well, thats a bit brain f*cks...