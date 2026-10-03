# Day 2 - Python Dictionaries

# Creating a dictionary
student = {
    "name": "Sneha",
    "age": 20,
    "course": "B.Tech",
    "is_student": True
}

print("Student Information:")
print(student)

# Accessing values
print("Name:", student["name"])
print("Course:", student["course"])

# Adding a new item
student["city"] = "Jaipur"
print("After adding city:", student)

# Updating a value
student["age"] = 21
print("Updated age:", student["age"])

# Removing an item
student.pop("is_student")
print("After removing is_student:", student)

# Loop through dictionary
print("Dictionary data:")

for key, value in student.items():
    print(key, ":", value)
