# Day 4 - Data Science Fundamentals

print("DATA SCIENCE FUNDAMENTALS")
print("-------------------------")

# What is Data Science?
print("\n1. What is Data Science?")
print("Data Science is the process of collecting, cleaning, analyzing,")
print("and interpreting data to find useful information and insights.")

# Main steps in Data Science
steps = [
    "Data Collection",
    "Data Cleaning",
    "Data Analysis",
    "Data Visualization",
    "Machine Learning",
    "Decision Making"
]

print("\n2. Steps in Data Science:")
for step in steps:
    print("-", step)

# Real-world applications
applications = {
    "Healthcare": "Disease prediction and patient monitoring",
    "Finance": "Fraud detection and risk analysis",
    "E-commerce": "Product recommendations",
    "Education": "Student performance analysis",
    "Transportation": "Traffic and route prediction"
}

print("\n3. Real-World Applications:")
for field, application in applications.items():
    print(field, ":", application)

# Python libraries used in Data Science
libraries = ["NumPy", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn"]

print("\n4. Common Python Data Science Libraries:")
for library in libraries:
    print("-", library)

print("\nLearning Outcome:")
print("I learned the basic concepts, steps, applications,")
print("and commonly used Python libraries in Data Science.")
