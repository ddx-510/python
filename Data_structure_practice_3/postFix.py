# stack_ linked list version

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def is_full(self):
        # impossible as we wont exceed the memory in linked list
        pass

    def push(self, data):  # insert
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
            print(curr.data)
            curr = curr.link


# main
value = stack()
string = input("Enter value with operators: ")
string = string.split()
for item in string:
    if item.isdigit() is True:  # if it is a number, push into slack
        value.push(int(item))
    else:
        # pop the last 2 numbers
        a = value.pop()
        b = value.pop()
        # check the operator, and do the operation
        if item == "+":
            c = b + a
        elif item == "-":
            c = b - a
        elif item == "*":
            c = b * a
        else:
            c = b / a
        # push back the value
        value.push(c)

print("result is : ", value.pop())
