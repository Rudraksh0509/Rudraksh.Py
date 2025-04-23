import csv

with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'])
    writer.writerow([101, 'Alice', 88, 90, 85])
    writer.writerow([102, 'Bob', 76, 89, 84])
print("CSV created successfully.")
