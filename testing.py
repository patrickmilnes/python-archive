from sll import SLL

ssl = SLL()

arr = [1, 2, 3, 4, 5]

ssl.prepend(1)
# print(ssl.head.value)

ssl.add_array(arr)
ssl.print()

ssl.delete(3)

print("NEW")
ssl.print()
print(ssl.count())
print(ssl.search(23))
