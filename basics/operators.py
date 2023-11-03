# Assignment operator
if __name__ == "__main__":
    j = 0
    for i in range(10):
        j += i
        print("=====")
        print("i", i)
        print("j", j)

    j /= 5
    print("Division", j)
    j *= 4
    print("Multiplication", j)

    j = "Now I am a..."
    j += "String"
    print(j)

    new_list = ["Obj"]
    new_list *= 3
    print(new_list)

    print(j := "Hello Word")
    if j == "Hello Word":
        print("reassigned")
    else:
        print("error")

    print((j + " ") * 5)

    for i in range(10):
        if i % 2 == 0:
            print("fizz", end="-")
        else:
            print("buzz", end="@")
