class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def isFull(self):
        pass

    def push(self, data):
        node = Node(data)
        node.link = self.top
        self.top = node

    def pop(self):
        if self.isEmpty() is True:
            print("Empty stack cannot delete")
            return -1
        else:
            data = self.top.data
            self.top = self.top.link
            return data

    def peek(self):
        if self.isEmpty() is not True:
            return self.top.data

    def display(self):
        curr = self.top
        while curr is not None:
            print(curr.data)
            curr = curr.link


# main function
stack1 = stack()
output = []
string = input("Enter the equation: ")
postfix = string.split()
for i in range(0, len(postfix)):
    # loop thru the input to see each case
    if postfix[i].isdigit() is True:
        # if number ,immediately output it
        output.append(postfix[i])
    else:
        # if open bracket, push it to stack
        if postfix[i] == "(":
            stack1.push(postfix[i])
        # if close bracket, output until see open bracket
        elif postfix[i] == ")":
            while stack1.peek() != "(" and stack1.isEmpty() is not True:
                output.append(stack1.pop())
            # the open bracket is still inside, pop it without appending to list
            stack1.pop()
        else:
            # encounter an operator
            while stack1.peek() != "(" and stack1.isEmpty() is not True:  # keep outerout until seeing open bracket
                # if current is * or /, the outermost element of stack must be * or /
                if (postfix[i] == "*" or "/") and ((stack1.peek() == "*") or (stack1.peek() == "/")) is True:
                    output.append(stack1.pop())
                # if current is + or -, outermost can be sign
                elif (postfix[i] == "+" or postfix[i] == "-") and (stack1.peek() == "+" or "-" or "*" or "/"):
                    output.append(stack1.pop())
                else:
                    # if no condition is met, end the loop
                    break
            # push the current element to stack
            stack1.push(postfix[i])

# check whether stack is empty and output all operators except ( or )
while stack1.isEmpty() is not True:
    if stack1.peek() != "(" or ")":
        output.append(stack1.pop())

# final output
for i in range(0, len(output)):
    print(output[i], end=" ")
