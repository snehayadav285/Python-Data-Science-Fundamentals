# Day 3 - Python File Handling

# Writing data to a file
with open("student_data.txt", "w") as file:
    file.write("Name: Sneha\n")
    file.write("Course: B.Tech\n")
    file.write("Subject: Python and Data Science\n")

print("Data written successfully.")

# Reading data from the file
with open("student_data.txt", "r") as file:
    data = file.read()

print("\nFile Content:")
print(data)

# Appending new data
with open("student_data.txt", "a") as file:
    file.write("Internship: CodoMax\n")

print("New data added successfully.")

# Reading the updated file
with open("student_data.txt", "r") as file:
    updated_data = file.read()

print("\nUpdated File Content:")
print(updated_data)
