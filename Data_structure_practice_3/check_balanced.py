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
            print(curr.data)
            curr = curr.link


class checkBalance:
    def answer(self):
        # check-balanced
        string = self
        stack = Stack()
        flag = True
        for i in range(0, len(string)):
            # if there is a open bracket, push it to stack
            if string[i] == "(" or string[i] == "[" or string[i] == "{":
                stack.push(string[i])

            # if there is a close bracket
            if string[i] == ")" or string[i] == "]" or string[i] == "}":
                # check whether empty, empty then not balanced
                if stack.is_empty() is True:
                    flag = False
                else:
                    # not empty,pop the stack
                    temp = stack.pop()
                    # check whether the brackets match each other
                    if (string[i] == ")" and temp == "(") or (string[i] == "]" and temp == "[") or (
                                    string[i] == "}" and temp == "{"):
                        pass
                    else:
                        flag = False

        if stack.is_empty() is False:
            flag = False

        if flag is True:
            return "Mathced"
        else:
            return "Not matched"
