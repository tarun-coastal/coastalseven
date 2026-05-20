import json


#  Convert Python Dictionary → JSON

student = {
    "name": "Tarun",
    "age": 21,
    "course": "Python"
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))


#  Convert JSON → Python Dictionary

import json

data = '{"name": "Tarun", "age": 21}'

python_data = json.loads(data)

print(python_data)
print(type(python_data))

# Write JSON Data to File
import json

employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 50000
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

print("JSON file created")


# Read JSON Data from File
import json

with open("employee.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])