import sys, json, datetime, re, os, ctypes, re, textwrap

# Make Console Free if Windows
if os.name == 'nt':
    kernel = ctypes.WinDLL('kernel32')
    hout = kernel.GetStdHandle(-11)
    mode = ctypes.c_ulong()
    kernel.GetConsoleMode(hout, ctypes.byref(mode))
    mode.value |= 4
    kernel.SetConsoleMode(hout, mode)

# Console Log
def log(type, text, color, newline = False):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "blue": "\033[34m"
    }

    if newline:
        print()

    return f"{colors[color]}[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {type}: {text}\033[00m"

# Load Config
with open("config.json", "r", encoding="utf-8") as f:
    configs = json.load(f)

memory_size = configs['MEM'] # Cell Size
memory, current, compiled = [0 for byte in range(memory_size)], 0, ""

# Check if 
if sys.argv[1]:
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
    except FileNotFoundError:
        print(log("ERROR", "File not found!", "red"))
        exit(1)
else:
    code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>." # Hello World Program

chars = ("+", "-", ">", "<", ".", ",", "[", "]", )
# Clear the Useless Chars
code = textwrap.wrap(''.join(filter(lambda x: x in chars, code)), 80)
logs = []

# Add Functions
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

# Compiling the Program
print(log("INFO", "Compiling Program to Python Code...", "blue"))
t_indent = 0
for index, char in enumerate('\n'.join(code)):
    if char == chars[0]:
        compiled += f"{' '*t_indent}change_byte(current, '+')\n"
        if configs['DEBUG']: logs.append(log("DEBUG", "Add 1 Byte to Current Cell", "green"))
    elif char == chars[1]:
        compiled += f"{' '*t_indent}change_byte(current, '-')\n"
        if configs['DEBUG']: logs.append(log("DEBUG", "Remove 1 Byte to Current Cell", "green"))
    elif char == chars[2]:
        compiled += f"{' '*t_indent}current = current + 1 if current < len(memory) - 1 else 0\n"
        if configs['DEBUG']: logs.append(log("DEBUG", "Goto Next Cell", "cyan"))
    elif char == chars[3]:
        compiled += f"{' '*t_indent}current = current - 1 if current > 0 else len(memory) - 1\n"
        if configs['DEBUG']: logs.append(log("DEBUG", "Goto Last Cell", "cyan"))
    elif char == chars[4]:
        compiled += f"{' '*t_indent}sys.stdout.write(chr(memory[current]))\n"
        if configs['DEBUG']: logs.append(log("DEBUG", "Print the Current Cell", "yellow"))
    elif char == chars[5]:
        compiled += f"{' '*t_indent}memory[current]=ord(input()[0])\n"
        if configs['DEBUG']: logs.append(log("DEBUG", "Input the 1 Byte to the Current Cell and Change", "yellow"))
    elif char == chars[6]:
        compiled += f"\n{' '*t_indent}while memory[current] != 0:\n"
        if configs['DEBUG']: logs.append(log("DEBUG", "Start the While Loop", "magenta"))
        t_indent += 4
    elif char == chars[7]:
        compiled += f"\n"
        if configs['DEBUG']: logs.append(log("DEBUG", "Finish the While Loop", "magenta"))
        t_indent -= 4

# Write the Logs.
if len(logs) > 0:
    # Print the logs
    print('\n'.join(logs))
    with open("logs.txt" if not 'LOG_FILE' in configs else configs['LOG_FILE'], "a+", encoding="utf-8") as f:
        f.write('\n'.join([log[5:len(log)-5] for log in logs]))

with open("compiler.py" if not 'COMPILE_FILE' in configs else configs['COMPILE_FILE'], "w+", encoding="utf-8") as f:
    f.write(f"""import sys
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

{compiled}
""")

# Run the Compiled Program
try:
    exec(compiled)
except Exception as e:
    result = input(log("ERROR", "An Error Detected While Running. If You Want to Dump, Please type \"y\". Else, Just Enter and See the Error: ", "red", True))
    if result.lower() == "y":
        pass
    else:
        raise e

print(log("INFO", f"Program Executed Successfully! Check {'dump.py' if not 'DUMP_FILE' in configs else configs['DUMP_FILE']} for Compiled Code!", "blue", True))
# Create Dump String
dumped = """# DUMP RESULT | {5}
# =======================================================
# TOTAL CELL GIVEN: {0}
# TOTAL CELL USED: {3}
# TOTAL BYTE USED: {2}
# MEMORY DUMP: [
{4}
# ]

# MINIFIED VERSION: [
{6}
# ]
# =======================================================

import sys
memory, current, indent, compiled = [0 for byte in range({0})], 0, 0, ""

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

{1}
""".format(
    memory_size, 
    compiled, 
    sum(memory),
    len([i for i in memory if i != 0]),
    '\n'.join('    # CELL_{0} -> {1} BYTE'.format(i, b) for i, b in enumerate(memory)),
    datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
    '\n'.join('    # LINE_{0} -> {1}'.format(i + 1, l) for i, l in enumerate(code))
)

# Write Dump
with open("dump.py" if not 'DUMP_FILE' in configs else configs['DUMP_FILE'], "w+", encoding="utf-8") as f:
    f.write(dumped)