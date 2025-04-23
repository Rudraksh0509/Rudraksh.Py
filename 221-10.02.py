import csv

student_data = {}

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        student_data[row['Roll No']] = {
            'Name': row['Name'],
            'Total': total
        }

print("Student Dictionary:", student_data)
