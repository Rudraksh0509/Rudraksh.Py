names = set()


names.update(["Amit", "Raj", "Neha", "Tina", "John"])
print("After adding names:", names)


names.remove("Raj")
names.add("Ravi")
print("After modifying Raj to Ravi:", names)


names.discard("Neha")
names.discard("Tina")
print("After deleting two names:", names)
