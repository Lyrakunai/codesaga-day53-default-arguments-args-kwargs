# Codesaga - Day 53
# Topic: Default Arguments, *args and **kwargs


# 1. Default Arguments

def greet(name, message="Welcome to Codesaga!"):
    print(f"{message} {name}")


greet("Nainu")
greet("Nainu", "Keep learning!")


# 2. *args - Collects Extra Positional Arguments

def calculate_total(*prices):
    total = 0

    for price in prices:
        total += price

    return total


print(calculate_total(100, 200, 50))
print(calculate_total(25, 75))


# 3. **kwargs - Collects Extra Keyword Arguments

def show_profile(name, **details):
    print("Name:", name)
    print("Additional Details:", details)


show_profile("Nainu", city="Patna", level="Intermediate")


# 4. Combining Parameters

def student_profile(name, age=18, *subjects, **details):
    print("Name:", name)
    print("Age:", age)
    print("Subjects:", subjects)
    print("Additional Details:", details)


student_profile(
    "Nainu",
    17,
    "Python",
    "AI",
    city="Patna",
    level="Intermediate"
)


# 5. Keyword-Only Parameter After *args

def create_profile(name, *skills, age=18, **details):
    print("Name:", name)
    print("Skills:", skills)
    print("Age:", age)
    print("Additional Details:", details)


create_profile(
    "Nainu",
    "Python",
    "Problem Solving",
    age=17,
    city="Patna"
)
