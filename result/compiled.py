import sys
memory, current, indent, compiled = [0 for byte in range(30000)], 0, 0, ""

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


