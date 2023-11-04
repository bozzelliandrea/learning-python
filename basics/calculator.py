import sys

from common.exceptions import InputException, InvalidModeException


def operation(op, mode):
    if not mode:
        raise InputException("Mode is null!")

    match mode:
        case '-c':
            return op(*input_read())
        case '-m':
            return daemon_read(op)
        case _:
            raise InvalidModeException(f"Input mode {mode} not valid")


def daemon_read(op):
    tot = 0
    while (p := input("value: ")) != '=':
        tot = op(tot, int(p))
        print(f'current: {tot}')
    return tot


def input_read():
    if a := input("First value: "):
        a = int(a)
    else:
        raise InputException("First value is null")

    if b := input("Second value: "):
        b = int(b)
    else:
        raise InputException("Second value is null")
    return [a, b]


def add(a=0, b=0):
    return a + b


def sub(a=0, b=0):
    return a - b


def div(a=0, b=0):
    return a / b


def mul(a=0, b=0):
    return a * b


"""
Simple math calculator
command list:
    > add: request 2 number and return the addition
    > sub: request 2 number and return the subtraction
    > mul: request 2 number and return the multiplication
    > div: request 2 number and return the division
    > help: print the command list
    > exit
flag list:
    > -m: multiple values, maintain the operation and insert infinite values, every number entered print delta
    > -c: couple values mode (default)
    > =: break the m mode and return the final result
"""
if __name__ == "__main__":
    print("PyCalc 2.0")
    while True:
        command = input("command: ")
        instructions = command.split(" ")
        if len(instructions) == 1:
            instructions.append("-c")
        match instructions[0]:
            case "help":
                print("add: request 2 number and return the addition",
                      "sub: request 2 number and return the subtraction",
                      "mul: request 2 number and return the multiplication",
                      "div: request 2 number and return the division",
                      "exit: exit from program",
                      "flag: flag manual list",
                      sep='\n')
            case "flag":
                print("-m: multiple values, maintain the operation and insert infinite values",
                      "-c: couple values mode (default)",
                      " =: break the m mode and return the final result",
                      sep='\n')
            case "add" | "sub" | "mul" | "div":
                f = getattr(sys.modules[__name__], instructions[0])
                print(operation(lambda a, b: f(a, b), instructions[1]))
            case "exit":
                exit(0)
            case _:
                print("Command not found, use 'help' command to show the command list")
