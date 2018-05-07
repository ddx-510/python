class Node:

    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self,new_data):
        return Node(new_data)

    def insert(self,new_data):
        new_node = self.add_node(new_data)
        # case 1 empty list
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            prev = curr
            # find correct position to insert
            while (curr is not None) and (curr.data < new_data):
                prev = curr
                curr = curr.link
            # case 2 front
            if prev == curr:
                new_node.link = curr
                self.head = new_node
            # case 3 end
            elif curr is None:
                prev.link = new_node
            else:# case 4 in between
                new_node.link = curr
                prev.link = new_node

    def delete(self,data):
        if self.head is None:
            print("Empty linked list")
        else:
            curr = self.head
            prev = curr
            # find correct node to delete
            while(curr is not None) and (curr.data < data):
                prev = curr
                curr = curr.link
            if curr.data != data: # check if data exists
                print("No such data")
            else:# adjust pointers
                prev.link = curr.link

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr =  curr.link




# main
# create new empty linked list
linkedlist1 = LinkedList()
# insert to empty linked list
linkedlist1.insert("Tom")
linkedlist1.insert("Alo")
linkedlist1.insert("Zenon")
linkedlist1.insert("Mom")
linkedlist1.delete("Tom")
linkedlist1.display()
