class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None #this points to the head of linked list

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head # this is the scavenger head, like the starting of the adventure
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
            print(llstr)


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >=self.get_length():
            raise Exception("Invalid index")

        if index ==0:
            self.head = self.head.next
            return

        count =0
        itr =self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            count +=1
            itr = itr.next

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")

        if index ==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

    def insert_after_value(self, data_after, data_to_insert):
        # search for first occurance of data_after in linked list
        # now insert data to insert after data_after
        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

            itr = itr.next

    def remove_by_value(self, data):
        # remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        prev =None

        while itr:
            if itr.data == data:
                prev.next = itr.next
                break
            prev = itr
            itr = itr.next




ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()



