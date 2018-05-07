class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        pass

    def push(self, data):
        node = Node(data)
        node.link = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            print("Cannot delete from an empty stack!")
            return -1
        else:
            data = self.top.data
            self.top = self.top.link
            return data

    def peek(self):
        return self.top.data

    def display(self):
        curr = self.top
        while curr is not None:
            print(curr.data, end="")
            curr = curr.link
        print()


# convert
n = int(input("Input a decimal number"))
stack2 = Stack()
stack8 = Stack()
stack16 = Stack()

# binary
temp = n
remainder = 0
while temp != 0:
    remainder = temp % 2
    stack2.push(remainder)
    temp //= 2
print("binary is: ", end="")
stack2.display()

# octal
temp = n
while temp != 0:
    remainder = temp % 8
    stack8.push(remainder)
    temp //= 8
print("octal is: ", end="")
stack8.display()

# hex
temp = n
while temp != 0:
    remainder = temp % 16
    if remainder >= 10:
        new_remainder = chr(remainder + 55)
        stack16.push(new_remainder)
    else:
        stack16.push(remainder)
    temp //= 16
print("hexa is: ", end="")
stack16.display()
