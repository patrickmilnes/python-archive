from sll import SLL
from node import Node

root = Node(34)
new1 = Node(78)
root.ref = new1
n1 = root
print(root.ref.value)
n1.ref = Node(45)
print(root.ref.value)