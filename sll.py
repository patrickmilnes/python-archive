from node import *

# head = None

# p = Node()
# p.value = 6
# # p.ref = head -> Does not have to be done on the first one.
# head = p

# print(head.ref)

# p = Node()
# p.value = 7
# p.ref = head
# head = p

# print(head.ref)
# print(head.value)

class SLL:

    def __init__(self):
        self.head = None

    def add_item(self, node):
        node.ref = self.head
        self.head = node

    def insert_item(self, node, node_before):
        node.ref = node_before.ref
        node_before.ref = node


    def append(self, data):
        if head == None:
            head = Node(data)
            return 0

        current = head
        while current.ref != None:
            current = current.ref
        
        current.ref = Node(data)
        return 0

    def prepend(self, data):
        new_head = Node(data)
        new_head.ref = self.head
        self.head = new_head

    def add_array(self, arr):
        for item in arr:
            self.prepend(item)
    
    def delete(self, data):
        if self.head == None:
            return
        if self.head.value == data:
            self.head = self.head.ref        
        current = self.head
        while current.ref != None:
            if current.ref.value == data:
                current.ref = current.ref.ref
                return
            current = current.ref

    def count(self):
        count = 0
        current = self.head
        while current.ref != None:
            count += 1
            current = current.ref

        return count


    def print(self):
        current = self.head
        while current.ref != None:
            print(current.value)
            current = current.ref

    
    def search(self, target):
        if self.head == None:
            return False
        current = self.head
        while current.ref != None:
            if current.ref.value == target:
                return True

            current = current.ref

        return False

