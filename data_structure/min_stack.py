'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''
class EmptyStack(Exception):
    def __init__(self):
        super().__init__("Stack is empty!")

class Node:
    def __init__(self, val: int, next: 'Node' = None, min_val: int = float("-inf")):
        self.val = val
        self.next = next
        self.min_val = min_val

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        node = Node(val)
        
        if self.isEmpty():
            node.min_val = node.val
        else:
            node.min_val = min(val, self.head.min_val)
        
        node.next = self.head
        self.head = node

    def pop(self) -> None:
        if self.isEmpty():
            raise EmtpyStack()

        node = self.head
        self.head = self.head.next
        del(node)

    def top(self) -> int:
        if self.isEmpty():
            raise EmptyStack()

        return self.head.val

    def getMin(self) -> int:
        if self.isEmpty():
            return EmptyStack()

        return self.head.min_val

    def isEmpty(self) -> bool:
        return self.head is None
