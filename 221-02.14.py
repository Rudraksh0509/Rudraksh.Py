grades = [
    (0, "NA"), (0, 39, "F"), (40, 44, "P"), (45, 49, "C"),
    (50, 54, "B"), (55, 59, "B+"), (60, 69, "A"),
    (70, 79, "A+"), (80, 100, "O")
]

def get_grade(mark):
    if mark == "Absent":
        return "NA"
    mark = int(mark)
    for g in grades:
        if len(g) == 2 and mark == g[0]:
            return g[1]
        elif len(g) == 3 and g[0] <= mark <= g[1]:
            return g[2]
    return "Invalid"

marks = []
for i in range(3):
    m = input(f"Enter marks for subject {i+1} (or 'Absent'): ")
    marks.append(m)

total = 0
valid_marks = 0
fail = False

for m in marks:
    if m == "Absent" or int(m) <= 39:
        fail = True
    if m != "Absent":
        total += int(m)
        valid_marks += 1

average = total / valid_marks if valid_marks else 0

print("Total:", total)
print("Average:", average)
print("Result:", "Fail" if fail else "Pass")

for i, m in enumerate(marks):
    print(f"Subject {i+1}: Grade {get_grade(m)}")
