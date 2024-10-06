# Basics of Python

---

                **`I N D E X`**

# Basic Concepts

## Mathematical Operations

- To do a calculation, you have to enter it into a print statement.
- **Rational Operators (outputs are [Boolean Operations](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21))**
    
    x==y: equal *(Checks if the values of two operands are equal or not, if yes then condition becomes true)*
    
    x!=y: *(Checks if the values of two operands are equal or not, if values are not equal then condition becomes true)*
    
    x>y: greater than *(Checks if the value of the left operand is greater than the value of the right operand, if yes then condition becomes true)*
    
    x<y: less than *(Checks if the value of the left operand is less than the value of the right operand, if yes then condition becomes true.)*
    
    x>=y: greater than or equal *(Checks if the value of the left operand is greater than or equal to the value of the right operand, if yes then condition becomes true.)*
    
    x<=y: less than or equal (Checks if the value of the left operand is less than or equal to the value of the right operand, if yes then condition becomes true.)
    
- Division results in a decimal at the end of your output
    
    ```python
    print((4 + 8) / 2)
    ```
    
- While putting spaces around an operation sign isn’t necessary, it does make reading code easier.
- Can use a minus sign to make a number negative (ex: -8)
- **Arithmetic Operators**
    
    x+y: addition *(Adds values on either side of the operator)*
    
    x-y: subtraction *(Subtracts the right hand operand from the left hand operand)*
    
    x*y: multiplication *(Multiplies values on either side of the operator)*
    
    - x**y: exponentiation (raises the right number to the power of the left number)
        
        ```python
        print(2 ** 5)
        ```
        
        - can chain together (x**y**z)
        - floats can also be used
            
            ```python
            print(9 ** (1 / 2))
            ```
            
        
    
    x/y: division *(Divides the left hand operand by the right hand operand, always turns into [float](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21))*
    
    - x % y: modulo/modulus *(finds remainder of a division)*
        
        ```python
        print(20 % 6)
        # 6 * 3 = 18 + 2 = 20
        ```
        
        - can also be used with floats
            
            ```python
            print(4.2 // 1.4)
            ```
            
    - x // y: floor division *(quantity produced by the division of two numbers as an integer, also called ‘quotient’)*
        
        ```python
        print(20 // 6)
        ```
        
        - can also be used with floats
            
            ```python
            print(1.25 % 0.5)
            ```
            

### In-Place Operators


In-place operators: allows code such as ‘x=x+3’ to be written more concisely, replacing the old variable being worked on, Can be used with any numerical operators (+, -, *, /, %, **, //) 

```python
x -= 2
x /= 3
x *= 5

```

can also be used for [string concatenation](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21)

```python
x = 'spam'
print(x)

x += 'eggs'
print(x)
```

- can use parentheses to indicate the operation you want done first
    
    ```python
    print(2 * (3 + 4))
    ```
    

---

## Data Types


| Data Name | Definition | Example |
| --- | --- | --- |
| String | text enclosed in single or double quotes | “Hello world” or ‘Hello world’ |
| Integer | whole numbers (can be used in mathematical operations) | 42 or 12 |
| Float | A decimal number, caused by division (can be used in mathematical operations) | 42.5 or 12.0 |
- when a float is added to an integer, it always comes out a float even with no remainder (ex: 12.0 + 4 = 16.0)
- dividing with a slash always causes a float, even if dividing integers

### Strings Explained

- everything in quotes (”_” or ‘_’) is a string, even numbers
- \ : escape character (represents things in a string such as new lines, tabs, and other useful things)
    
    ```python
    print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')
    print("He said: \"cool!\".")
    # can usually just switch quotation type to not have to do this
    print("Brian's mother: He's not an angel. He's a very naughty boy!")
    print('He said: "cool!".')
    ```
    
    ```python
    print('One \n Two \n Three')
    ```
    
    ```python
    print("\t hey \t there")
    ```
    
    ```python
    print("Hi \r there")
    ```
    
    ```python
    print("newline is \\n")
    ```
    
    windows uses \r\n to signify the enter key, while linux & unix uses \n
    
- same as newline, but less repetitive, is the three quotes
    
    ```python
    print("""this
    is a
    multiline
    text""")
    ```
    
    -in this format, quotes don’t need the escape character to be correctly formatted
    
- to make a string repeat itself on the same line, program print(’string’ * integer)
    - cannot do string + integer
    - cannot do string * string
    - cannot so string * float
- adding strings together is called concatenation

---

## Comments & Docstrings


- Comments are annotations to code using an octothorpe ( # ) to help explain what’s going on in your code or to add notes.  Any text after using # will be ignored and not applied to your code
    
    ```python
    # this is a comment
    ```
    
- docstrings can be done to add multiple lines of comments explaining of a [function](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21) below the functions first line, acting as documentation for other developers who use your function. Unlike comments, docstrings can be inspected at run time (or when your code has been run).
    
    ```python
    def shout(word)
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + '!')
    ```
    

---

## Print Command


The print command is made to give a specific output when a program is ran, whether that be string, functions, or numbers.

**Rules of the print command are:**

```python
print("Hello world")
print('Hello world')
# since there are two lines of print, there will be two different outputs
```

1. must be followed by parenthesis
2. If it contains a [string](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21), that string must be embedded inside quotations (also called delimiters)
    1. single or double quotes will work
3. To put multiple messages in a program, a new print command must be added to a new line

---

---

# Variables


a variable lets you store a value by assigning it to a name. the name can be used to refer to the value later in the program

```python
user = "James"
```

- = : assignment operator
    - can assign any type of value to variable, including integers, strings, and floats
- can use letters, numbers, and underscores in variable names. cannot use special symbols, or start it with a number
    - python is case sensitive (Lastname and lastname are two different variable names)

---

## Working w/ Variables


once you have an established variable, you can now use them to perform corresponding operations

```python
x = 7
print(x)

print(x + 3)
print(x)
```

to reestablish a variable, just rename it

```python
x = 123.456
print(x)

x = "this is a string"
print(x  + "!")
```

use the del statement to remove a variable from your program

```python
x = 42
del x
```

---

---

# Control Flow


## Booleans Explained

Booleans is a data type that comes out to only two values - True and False. Boolean values will always be capitalized! When you see True or False in these notes, it will always be referring to Boolean statements.

To use a Boolean, we use the equal operator (==) and compare values

```python
print(2 == 3)
#output - False
print("hello" == "hello")
#output - True
```

Greater than (>) and smaller than (<) operators can be used to compare strings lexicographically as well

```python
'a' > 'b'
'Bob' > 'Dave'
```

True and False can also be represented as integers as well (True turns into 1, False into 0), using the int() function

```python
x = (7 > 5)
print(int(x))
```

- **Practice Question:** Take two [inputs](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21) from user and check whether they are equal or not. toggle for answer
    
    ```python
    print("Enter first number")
    first = input()
    print("Enter second number")
    second = input()
    print(first == second)
    ```
    

### Boolean Logic


Boolean operators allow the combination of multiple conditions

- and operator: True only if both conditions evaluate to True
    
    ```python
    print(1 == 1 and 2 ==2
    # True
    print(1 == 1 and 2 == 3)
    # False
    print(1 != 1 and 3 > 6)
    # False
    ```
    
- or operator: True if either or both of its conditions are True, and False if both conditions are False
    
    ```python
    print(1 == 1 or 2 == 2)
    # True
    print(1 == 1 or 2 == 3)
    #True
    print(1 != 1 or 3 > 6)
    # False
    ```
    
- not operator: inverts the argument (not True is False, not False is True)
    
    ```python
    print(not 1 == 1)
    #False, because 1 == 1 is True, so you invert the answer with the not       operator
    print(not 1 > 7)
    #True, since 1 isn't greater than 7
    
    ```
    

can also compare variables to form conditions

```python
age = 24
limit = 18
height = 191
if (age > limit and height > 180):
	print("yes")
```

Can use Boolean logic to chain multiple conditional statements in an if statement using Boolean operators

```python
country = "US"
age = 42
if(country == "US" or country == "GB") and (age > 0 and age < 100):
	print('Cool')
```

*note: Pythons order of operations follows PEMDAS

```python
if not True:
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")
```

---

## If Statements


- **If statement rules**
    
    Statements in the if should be indented
    
    Leave a colon at the end of the expression in the if statement
    
    ```python
    if condition:
    		statements
    ```
    
- Can be used with [Boolean statements](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21) to run code based on a certain condition, for example if the Boolean evaluates to True

```python
# if statement example
x = 42
if x > 5:
		print("x is greater than 5")
```

By using indentation, we can “nest” if statements together to create more complex checks

```python
num = 12
if num > 5:
		print("Bigger than 5")
		if num <= 47:
				print("Between 5 and 47")
```

---

## Else/Elif Statements


**Else statements** can be used to run statements when the condition of the if statement is False

```python
x = 4
if x == 5:
	print("yes")
else:
	print('no')
```

else statements also need a colon at the end, along with all conditions being indented

- every if condition can only have one else statement. to have multiple checks, chaining if and else statements is necessary
    
    ```python
    num = 3
    if num == 1:
    	print('One')
    else:
    	if num == 2:
    		print(('Two')
    	else:
    		print(('Something else')
    ```
    

**Elif (short for else if) statements** are used to prevent making too many chained if/else statements, making your code long and hard to read. 

```python
num = 3
if num == 1:
	print('One')
elif num == 2:
	print('Two')
elif num == 3:
	print('Three')
else:
	print('Something else')
```

- Practice Q: Write a program to control entrance to a club. Only people who are 18 or older are allowed to enter the club. Your program takes the age of the person who tries to enter, and outputs "Allowed" if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age. toggle for answer
    
    ```python
    age = int(input())
    if age >= 18:
        print('Allowed')
    else:
        print('Sorry')
    ```
    

---

## While Loops


While loops allow you to repeat a block of code multiple times.

```python
i = 1
while i <=5:
	print(i)
	i = i + 1
print('Finished!')
#while i is less than 5, i will be incremented by 1 until it reaches 5. Executes print statement 5 times.
```

while loop statements will be indented just like [if statements](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21)

can also use if statements in while loops

```python
x = 1
while x < 10:
	if x%2 == 0:
	print(str(x) + ' is even')
else:
	print(str(x) + ' is odd')
x += 1
```

if the condition for a while loop remains True, the loop will run indefinitely because it has no statement causing it to end.

While True statement is an easy way to cause an infinite loop

```python
i = 0
while True:
	print(i)
i = i + 1
```

### Break Statements


Break statements end a while loop prematurely if a defined condition is met. Using the break statement outside of a loop causes an error.

```python
i = 0
while True:
	print(i)
	i = i + 1
	#defined condition
	if i >= 5:
	print('breaking')
	# break statement
	break

```

A realistic use of the break statement would be if your program was needing to infinitely take input from your user, until they enter ‘stop’

### Continue Statements


This loop statement, unlike the break statement that stops a loop, makes the output jump back to the start of a while loop to restart it

```python
i = 0
while i<5:
	i += 1
	if i == 3:
		print('Skipping 3')
		continue
	print(i)
```

Example case above: An airline ticketing system needs to calculate the total cost for all tickets purchased. Tickets for children under the age of 3 are free. We can use a while loop to iterate through the list of passengers and calculate the total cost of their tickets. Here, the continue statement can be used to skip the children.

---

---

# Lists


Lists used to store items. created by placing elements inside square brackets `[]`, separated by commas. Lists can hold different data types such as strings and numbers.

```python
words = ['Hello', 'world', '!']
nums = [1, 2, 3, 4]
```

to access a certain item in a last, use it’s index in square brackets. An index starts with 0 instead of 1

```python
words = ['Hello', 'world', '!'}
print(words[0])
print(words[1])
print(words[2])
```

- Using matrices inside lists
    
    to access elements of a matrice, we specify the row and the column of the item using square brackets
    
    ```python
    m = [
    		[1, 2, 3]
    		[4, 5, 6]
    		]
    # print(m[row][column])
    print(m[1][2])
    ```
    

Strings are able to be indexed like lists as well, where each character inside a string can be indexed or counted. If a string contains spaces, those also count inside an index.

```python
#      0123456789...
str = 'Hello world!'
print(str[8])
```

---

## List Operations


designated indexes can be reassigned

```python
nums = [5, 8, 2]
nums[1] = 42
print(nums)
```

```python
nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])
```

lists can also be added together

```python
nums = [1, 2, 3]
print(nums + [4, 5, 6])
```

lists can be multiplied by [integers](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21)

```python
nums = [1, 2, 3]
print(nums * 3)
```

we check if an item is in a particular list by using the in operator. This returns a Boolean value, True if the item is in the list, and False if it’s not included. Also can be used to determine if a substring is included inside the string (or not included with the not operator).

```python
words = ['spam', 'egg', 'spam', 'sausage']
print('spam' in words)
# True
print('tomatoes' in words)
# False
```

```python
x = 'hello world'
if 'world' in x:
	print('Yes')
```

```python
nums = [1, 2, 3]
print(not 4 in nums)
# or
print(4 not in nums)
```

---

## List Slices


List slices helps get a part of a list using two colon-separated indices, returning a new list containing all values between the indices. Just like [ranges](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21), the first index is included in the result, but not the second

```python
sqs = [0, 1, 4, 9, 16, 25]
print(sqs[2 : 5])
# output - [4, 9, 16]
```

if the first number in a slice is not given, its read as being the start of the list. same as if the last number is omitted, it outputs until the last number

```python
sqs = [0, 1, 4, 9, 16, 25]
print(sqs[:5])
# output- [0, 1, 4, 9, 16]
print(sqs[1:])
# output- [1, 4, 9, 16, 25]
```

list slices can also include a third number representing the jump between numbers you want to include.

```python
sqs = [0, 1, 4, 9, 16, 25]
print(squares[::2])
# output- [0, 4, 16]
print(squares[2 : 8 : 3])
# output- [4, 25]
```

if a negative number is used as a step, the slice counts backwards

```python
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])
# output- [49, 36]
```

---

## For Loops


For loops are used to iterate over a given sequence such as [lists](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21) or [strings](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21)

```python
words = ['hello', 'world', 'spam', 'eggs']
# for [variable that seperates each list item] in [combined list variable]
for word in words:
	print(word + '!')
```

for loop defines a variable that takes the value of the current item of the list on each iteration and allows you to do something with each item, such as when you add an exclamation to each list item in the example above

```python
# program to count the amount of times a letter appears
str = 'testing for loops'
count = 0

for x in str:
	if(x == 't'):
		count += 1
print(count)
```

the break and continue statements can be used in for loops to stop the loop or jump to the next iteration (colors correspond to colored code below).

```python
text = 'some text'
for x in text:
	if x == 'e':
		break
	print(x)
# output - som
# by replacing break with continue, output - somtxt
```

---

## Range


 range() function creates number sequences. starting from 0, it increments by 1 and stop before the specified number.

```python
numbers = range(10)
# output - range(0, 10)
```

to turn a range into a [list](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21), you have to include the list() function

```python
number = list(range(10))
print(numbers)
# output - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

there’s a Step argument, that determines the interval of the sequence produced. Using a negative number with this argument allows decreasing numbers.

```python
nums = list(range(5, 20, 2))
print(nums)
# output - [5, 7, 11, 13, 15, 17, 19]
x = list(range(7, 3, -1)
print(x)
# output - [7, 6, 5, 4]
```

range can also be used in ‘for loops’, you don’t need to convert them into lists. It’s used to repeat code a designated number of times

```python
for i in range(5);
	print('hello!')

# output- hello! || hello! || hello! || hello! || hello! 
```

for i in range() can also be used when using ‘returning functions’ and ‘for loops’.

---

---

# Functions


a function is a group of related statements that performs a specific task. Breaks program into smaller chunks to help make it more organized and manageable. Helps avoid repetition and makes code reusable.

- Has a name
- Can have arguments
    
    example: print(”hello!”)
    

Python has many built in functions, such as print, range, str

- Functions can have multiple arguments: range(2, 20)
    - need to be separated by commas
- you call the function by using it’s name, followed by (), which encloses the arguments
    
    ```python
    print("some text")
    # call the print function with a string argument to generate output
    ```
    
    ---
    

## List Functions


- **len()** : outputs the number of items in a list
    
    ```python
    nums = [1, 3, 5, 2, 4]
    print(len(nums))
    ```
    
    unlike indexing, len doesn’t start with 0
    
    ```python
    letters = ['a', 'b', 'c']
    letters += ['d']
    print(len(letters))
    ```
    
    can also use len to return the character count (including spaces) of a string
    
    ```python
    str = 'some text'
    x = len(str)
    print(x)
    ```
    
- **append()** : adds an item to the end of a list
    
    called using the list name, followed by a dot
    
    ```python
    nums = [1, 2, 3]
    nums.append(4)
    print(nums)
    ```
    
- **insert():** adds an item at a given position in the list
    
    ```python
    words = ['Python', 'fun']
    words.insert(1, 'is')
    print(words)
    ```
    
    called using the list name, followed by a dot
    
    ^the first argument is the position index, second is the item to insert
    
    ```python
    nums = [9, 8, 7, 6, 5]
    nums.append(4)
    nums.insert(2, 11)
    #[9, 8, 11, 7, 6, 5, 4] 
    print(len(nums))
    
    ```
    
- **index()**: finds the first occurrence of a list item and returns its index
    
    ```python
    letters = ['p', 'q', 'r', 's', 'p', 'u']
    print(letters.index('r'))
    ```
    
    called by using list name followed by a dot
    
    error output is returned if item cannot be found
    
- **max(list)/min(list)**: returns maximum/minimum value
    
    ```python
    x = [1, 8, 42, 3]
    
    print(min(x))
    print(max(x))
    ```
    
    ```python
    nums = [1, 3, 5, 2, 4]
    res = min(nums) + max(nums)
    # res = 1 + 5
    print(res)
    
    ```
    
    lower case letters have lower prioritization than uppercase when using max, so if you’re asked
    
    ```python
    txt = ‘Pool’
    print(max(txt)
    ```
    
    o would be the max value, while when using min you would prioritize uppercase letters making P the min value
    
- **remove()**: takes given element out of list
    
    ```python
    list = [8, 4, 2, 6]
    list.remove(2)
    ```
    
- **count()**: prints how many times an item is given in the list
    
    ```python
    list = [8, 4, 2, 6]
    list.count(6)
    ```
    

---

## [String Functions](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21)


- **input()** is a string function, allowing users to write out their own answer to a prompt
    
    By default input() comes out as a string, but if you want it to become an integer or float, you have to typecast it (examples below). You can prompt the user with a question, insert a : symbol afterwards and make sure to leave a space afterwards.
    
    ```python
    # Taking input as string
    color = input("What color is rose?: ")
    print(color)
     
    # Taking input as int
    # Typecasting to int
    n = int(input("How many roses?: "))
    print(n)
     
    # Taking input as float
    # Typecasting to float
    price = float(input("Price of each rose?: "))
    print(price)
    ```
    
- Strings have a **format()** function, enabling values to be listed in a chosen way
    
    ```python
    nums = [4, 5, 6, 7, 8, 9]
    msg = "Numbers: {0}-{1}-{2}" . format(nums[3], nums[1], nums[5])
    print(msg)
    
    # "Numbers: 7-5-9"
    ```
    
    can also name placeholders instead of index numbers
    
    Each argument of the **format**  function is placed in the string at the corresponding position, which is determined using the curly braces { }.
    
    ```python
    print("{0}{1}{0}".format("abra", "cad"))
    #                           0      1
    
    # "abracadabra"
    ```
    
    ```python
    a = "{x}, {y}".format(x=5, y=12)
    print(a)
    
    # "5, 12"
    ```
    
- strings also have a **join()** function that joins a list of strings with another string as a separator
    
    ```python
    x = ',' .join(['spam', 'eggs', 'ham'])
    print = (x)
    
    # "spam, eggs, ham"
    ```
    
- **split()** is the opposite of join(), meaning it turns a string into a list by using a separator
    
    ```python
    str = 'some text goes here'
    x = str.split(' ')
    print(x)
    
    # 'some', 'text', 'goes', 'here'
    ```
    
- **replace()** is also a function that causes one substring in a string to be replaced by another
    
    ```python
    x = 'hello me!'
    print(x . replace("me", "world"
    
    # "hello world!"
    ```
    
- **lower()** and **upper()** chane the case of a string to lowercase and uppercase letters
    
    ```python
    print('this is a sentence.' .upper())
    print('AN ALL CAPS SENTENCE' .lower())
    
    # 'THIS IS A SENTENCE.'
    # 'an all caps sentence'
    ```
    

---

## Making Your Own Functions


You can create your own functions using a **def** statement. Just like [if statements](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21), the code block within every function starts with a colon (:) and is indented.

The function below takes no arguments, and prints ‘spam’ three times

```python
def my_func():
		print('spam')
		print('spam')
		print('spam')
```

to call a function, we use its name and the parentheses, and once it’s defined we can call it multiple times

```python
def hello():
		print("hello world!")

hello()
hello()
hello()

# hello world!
# hello world!
# hello world!
```

- real world use practice!
    
    design a given function so that it will take the name of the user as [input](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21) and output a welcome message with it.
    
    ```python
    print("enter name below")
    user = input()
    def welcome():
       print("Welcome, " + user)
    
    welcome()
    ```
    

---

## Function Arguments


functions can take arguments, which can be used to generate the function output. Arguments are used to pass info to the function, allowing the reuse of the function logic for different values.

in this example, the argument is going to be named word.

```python
def exclamation(word):
		print(word + '!')

exclamation('spam')
exclamation('eggs')
exclamation('python')

# 'spam!'
# 'eggs!'
# 'python!'
```

another example with two arguments is:

```python
def print_sum_twice(x, y):
		print(x + y)
		print(x + y)

print_sum_twice(5, 8)

# 13
# 13
```

another argument using if/else statements:

```python
def even(x):
		if x%2 == 0:
				print('Yes')
		else:
				print('No')
```

---

## Returning From Functions


returning a function is used when you don’t need to output a variable, but rather assigns a result to a variable.

```python
def sum(x, y)
		return x + y

res = sum(42, 7)
print(res)
```

```python
def foo(x, y):
		if x>=y:
				return x
		else:
				return y

x = foo(4, 7)
print(x)

# 7
```

```python
def foo(x, y):
		if x>=y:
				return x
		else:
				return y

if (foo(6, 4) > 10):
		print('Yes')
else:
		print('Nope')

# Nope
```

once you return a value from a function, any code placed after the return statement wont be executed

```python
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))
```

so if you need to return multiple value, use a list:

```python
def double(a, b):
   return [a*2, b*2]

x = double(6, 9)
print(x)

# [12, 18]
```

you can also return a function using [‘for i in range’](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21):

```python
def sum(x):
		res = 0
		for i in range(x):
				res += i
		return res

print(sum(4))

# 6
```

because we are using a for loop with +=, the process looks like this until we get over or equal to 4

0 + 0 = 

0 + 1 = 

1 + 2 = 

3 + 3 = 6

---

---

# Collection Types


## Dictionaries

Python has collection types which allow you to store multiple values. [Lists](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21) are one of these types, which allow you to store indexed values which are automatically set:

```python
x = ['hi', 'hello', 'welcome']
print(x[2]) # [2] is the index

# the indexed value is 'welcome'
```

Dictionaries are one of these collection types as well, allowing you to map arbitrary keys to values, being indexed using square brackets containing developer set keys. Each element is represented by a **key : value** pair

```python
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
```

Only immutable (unable to change) objects can be used as keys in dictionaries. Which means, lists are unable to be used as keys.

to take a key as input and output the corresponding value, you must define a new variable as input() and print the given dictionary with the new variable:

```python
car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

info = input()
print(car[info])
```

---

## Dictionary Functions


Determining whether a key is in a dictionary, you can use [in and not in](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21), just as you can for a list.

```python
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
# True
print("three" in nums)
# False
print(4 not in nums)
# True
```

can use if statements as well to not get [Boolean](https://www.notion.so/Basics-of-Python-24af9955573f4e6a91564c2c4fba1422?pvs=21) output

```python
pairs = {
		125: "jdksn"
		41: "sjllnd"
		112: "iuefw"

if 112 in pairs:
		print('Yes')
```

---

---

# External Links for Learning

[GeekforGeeks.com](https://www.geeksforgeeks.org/python-programming-language/?ref=shm) : I just linked the (extensive) Python database they have, but they have numerous other programming language databases, along with job readiness articles, practice problems/projects, and paid courses if that’s your jam

 [websetup.org](https://websitesetup.org/python-cheat-sheet/) : Python cheat sheet (other programming langauage cheat sheets to the side)

[Codecademy.com](https://www.codecademy.com/resources/cheatsheets/language/python): Python cheat sheets

[Codecademy.com](https://www.codecademy.com/catalog/language/python): free Python courses (first one labeled ‘Course” instead of “Free Course’, lets you do only a couple sections for free and then doesn’t let you finish wihout a subscription

[Programming with Mosh](https://www.youtube.com/watch?v=kqtD5dpn9C8&t=359s) (1 hr): Beginners guide for Python that goes over the basics

[Programming with Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=6890s) (6 hr 14 min): Full beginners course for Python

[@SuperSimpleDev](https://www.youtube.com/@SuperSimpleDev/featured)//youtube: A youtube channel that I absolutely adore if you’re thinking about doing web development. While not Python related, he has an extensive HTML & CSS tutorial that is really easily understandable

[Python Discord](https://github.com/mhxion/awesome-discord-communities/blob/main/README.md#python) (Github list): A short list of python discords if that’s your thing (scrolling leads to discord servers for other programming languages)
