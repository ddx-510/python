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
        # handle 4 cases
        if self.head == None:  # empty list
            self.head = new_node
        else:
            curr = self.head
            prev = curr
            # find correct position to insert
            while (curr != None) and (curr.data < new_name):
                prev = curr
                curr = curr.link
            if prev == curr:  # insert to front
                new_node.link = curr
                self.head = new_node
            elif curr == None:  # insert to end
                prev.link = new_node
            else:  # insert in between
                new_node.link = curr
                prev.link = new_node

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
            if curr.data != name:  # check if name exists
                print("No such name.")
            else:  # display name
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
            if curr.data != old_name:  # check if name exists
                print("No such name.")
            else:  # edit name
                if prev == curr:
                    self.head = curr.link
                    self.Insert(new_name)
                    print(old_name + " updated into " + new_name)
                else:
                    prev.link = curr.link
                    self.Insert(new_name)
                    print(old_name + " updated into " + new_name)

    def Delete(self, name):
        if self.head is None:
            print("Empty list.")
        else:
            curr = self.head
            prev = curr
            # find correct node to delete
            while (curr is not None) and (curr.data < name):
                prev = curr
                curr = curr.link
            if curr.data != name:  # check if name exists
                print("No such name.")
            elif prev == curr:
                self.head = curr.link
                print(name + " deleted")
            else:  # delete node
                prev.link = curr.link
                print(name + " deleted.")

    def Display(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.link

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            link = curr.link
            curr.link = prev  # None, first time round.
            prev = curr  # Used in the next iteration.
            curr = link  # Move to next node.

        self.head = prev


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
print()

linkedlist.Edit("Amy", "Dabbi")
linkedlist.Display()
print()

linkedlist.reverse()
linkedlist.Display()
