faculty_names = ["Dr. Smith", "Dr. Jonathan", "Professor Xavier", "Anjali", "Dr. Elizabeth"]

long_names = list(filter(lambda x: len(x) > 8, faculty_names))
print("Names with more than 8 characters:", long_names)
