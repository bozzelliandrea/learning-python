from common.exceptions import InputException


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


def add():
    i = input_read()
    return i[0] + i[1]


def sub():
    i = input_read()
    return i[0] - i[1]


def div():
    i = input_read()
    return i[0] / i[1]


def multiply():
    i = input_read()
    return i[0] * i[1]


"""
Simple math calculator
command list:
    - add: request 2 number and return the addition
    - sub: request 2 number and return the subtraction
    - mul: request 2 number and return the multiplication
    - div: request 2 number and return the division
    - help: print the command list
    - exit
"""
if __name__ == "__main__":
    print("Welcome")
    while True:
        command = input("command: ")
        match command:
            case "help":
                print("add: request 2 number and return the addition",
                      "sub: request 2 number and return the subtraction",
                      "mul: request 2 number and return the multiplication",
                      "div: request 2 number and return the division",
                      "exit: exit from program",
                      sep='\n')
            case "add":
                print(add())
            case "sub":
                print(sub())
            case "mul":
                print(multiply())
            case "div":
                print(div())
            case "exit":
                exit(0)
            case _:
                print("Command not found, use 'help' command to show the command list")
