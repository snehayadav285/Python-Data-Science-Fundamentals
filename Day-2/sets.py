# Day 2 - Python Sets

# Creating a set
fruits = {"Apple", "Banana", "Mango", "Apple"}

print("Fruits:", fruits)

# Adding an element
fruits.add("Orange")
print("After adding Orange:", fruits)

# Removing an element
fruits.remove("Banana")
print("After removing Banana:", fruits)

# Checking membership
print("Is Mango present?", "Mango" in fruits)

# Finding the number of elements
print("Number of fruits:", len(fruits))

# Loop through a set
print("All fruits:")
for fruit in fruits:
    print(fruit)
