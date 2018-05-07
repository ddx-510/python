class Node:
    def __init__(self, name):
        self.data = name
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None

    def AddNode(self, new_name):
        return Node(new_name)

    def Insert(self, new_name):
        new_node = self.AddNode(new_name)
        new_node.link = self.head
        self.head = new_node


    def Search(self, name):
        if self.head == None:
            print("Empty list.")
        else:
            curr = self.head
            prev = curr
            # find correct node
            while (curr != None) and (curr.data < name):
                prev = curr
                curr = curr.link
            if curr.data != name: # check if name exists
                print("No such name.")
            else: # display name
                print(curr.data + " found.")

    def Edit(self, old_name, new_name):
        if self.head == None:
            print("Empty list.")
        else:
            curr = self.head
            prev = curr
            # find correct node to edit
            while (curr != None) and (curr.data < old_name):
                prev = curr
                curr = curr.link
            if curr.data != old_name: # check if name exists
                print("No such name.")
            else: # edit name
                curr.data = new_name
                print(curr.data + " updated.")

    def Delete(self, name):
        if self.head == None:
            print("Empty list.")
        else:
            curr = self.head
            prev = curr
            # find correct node to delete
            while (curr != None) and (curr.data < name):
                prev = curr
                curr = curr.link
            if curr.data != name: # check if name exists
                print("No such name.")
            else: # delete node
                prev.link = curr.link
                print(name + " deleted.")

    def Display(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.link


# main
# create new empty linked list
linkedlist = LinkedList()

# insert to empty list
linkedlist.Insert("Bob")

# insert to front
linkedlist.Insert("Amy")

# insert to end
linkedlist.Insert("Tom")

# insert in between
linkedlist.Insert("May")
linkedlist.Display()
