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
        if self.head is None:  # empty list
            self.head = new_node
            new_node.link = self.head
        else:
            curr = self.head
            curr = curr.link
            prev = curr
            # find correct position to insert
            while (curr != self.head) and (curr.data < new_name):
                prev = curr
                curr = curr.link

            if prev == curr:  # insert to front
                new_node.link = self.head
                self.head = new_node
                curr.link.link = self.head

            elif curr == self.head:  # insert to end
                prev.link = new_node
                new_node.link = curr

            else:  # insert in between
                new_node.link = curr
                prev.link = new_node


    def Search(self, name):

        if self.head == None:
            print("Empty list.")
        else:
            curr = self.head
            curr = curr.link
            prev = curr
            # find correct node
            while (curr != self.head) and (curr.data < name):
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

            if curr.data == old_name: # edit the head
                print(old_name + " updated into " + new_name)
                self.head = curr.link
                curr = curr.link

                while curr.link != self.head:
                    prev = curr
                    curr = curr.link
                prev.link = self.head
                self.Insert(new_name)
            else: # find correct node to edit

                curr = curr.link
                while (curr != self.head) and (curr.data < old_name):
                    prev = curr
                    curr = curr.link
                if curr.data != old_name:  # check if name exists
                    print("No such name.")
                else:  # edit name
                    prev.link = curr.link
                    self.Insert(new_name)
                    print(old_name + " updated into " + new_name)


    def Delete(self, name):
        if self.head is None:
            print("Empty list.")
        else:
            curr = self.head
            prev = curr

            if curr.data == name: # delete the head
                print(name + " deleted")
                self.head = curr.link
                curr = curr.link
                while curr.link != self.head:
                    prev = curr
                    curr = curr.link
                prev.link = self.head

            else:
                curr = curr.link
            # find correct node to delete not at head
                while (curr != self.head) and (curr.data < name):
                    prev = curr
                    curr = curr.link
                if curr.data != name:  # check if name exists
                    print("No such name.")
                else:  # delete node
                    prev.link = curr.link
                    print(name + " deleted.")

    def Display(self):
        curr = self.head
        print(curr.data)
        curr = curr.link
        while curr != self.head:
            print(curr.data)
            curr = curr.link
        print(curr.data)



# main
# create new empty linked list
linkedlist = LinkedList()

# insert to empty list
linkedlist.Insert("Bob")

# insert to front
linkedlist.Insert("Amy")


linkedlist.Insert("DD")

linkedlist.Insert("A")
linkedlist.Insert("E")



linkedlist.Display()
