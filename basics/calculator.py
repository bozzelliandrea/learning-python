def input_read():
    return [input("First value: "), input("Second value: ")]


def add():
    i = input_read()
    return int(i[0]) + int(i[1])


def sub():
    i = input_read()
    return int(i[0]) - int(i[1])


def div():
    i = input_read()
    return int(i[0]) / int(i[1])


def multiply():
    i = input_read()
    return int(i[0]) * int(i[1])


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
