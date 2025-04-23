import pickle

employee = {
    "empcode": "E101",
    "empname": "John Doe",
    "doj": "2021-06-01",
    "salary": 55000
}

# Serialize
with open('employee.pkl', 'wb') as file:
    pickle.dump(employee, file)

# Deserialize
with open('employee.pkl', 'rb') as file:
    loaded_employee = pickle.load(file)

print("Deserialized Employee:", loaded_employee)
