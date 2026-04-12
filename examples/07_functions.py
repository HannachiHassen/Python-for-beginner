# ============================================================
# 07 - Functions in Python
# ============================================================
# A function is a reusable block of code that does one job.
# Define once, use many times!

# ============================================================
# Defining and Calling a Function
# ============================================================
def greet():
    print("Hello, World!")

greet()   # call the function → Hello, World!

# ============================================================
# Parameters and Arguments
# ============================================================
def greet_person(name):        # 'name' is a parameter
    print(f"Hello, {name}!")

greet_person("Alice")          # 'Alice' is the argument
greet_person("Bob")

# Multiple parameters
def add(a, b):
    print(a + b)

add(3, 5)    # 8

# ============================================================
# Return Values
# ============================================================
def square(n):
    return n ** 2

result = square(6)
print(result)        # 36

# Return multiple values (as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 4, 7])
print(low, high)     # 1 9

# ============================================================
# Default Parameter Values
# ============================================================
def greet_with_message(name, message="Welcome!"):
    print(f"{name}: {message}")

greet_with_message("Alice")               # Alice: Welcome!
greet_with_message("Bob", "Good morning") # Bob: Good morning

# ============================================================
# Keyword Arguments
# ============================================================
def describe_pet(name, species, age):
    print(f"{name} is a {age}-year-old {species}.")

describe_pet(name="Luna", species="cat", age=3)   # order doesn't matter
describe_pet(age=5, name="Rex", species="dog")

# ============================================================
# *args → accept any number of positional arguments
# ============================================================
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))       # 6
print(total(10, 20, 30, 40))# 100

# ============================================================
# **kwargs → accept any number of keyword arguments
# ============================================================
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="NYC")

# ============================================================
# Scope: Local vs Global Variables
# ============================================================
x = "global"

def show_scope():
    x = "local"      # different variable, only lives inside this function
    print(x)         # local

show_scope()
print(x)             # global (unchanged)

# ============================================================
# Lambda Functions (anonymous one-liners)
# ============================================================
double = lambda n: n * 2
print(double(5))     # 10

add = lambda a, b: a + b
print(add(3, 4))     # 7

# Often used with sorted(), map(), filter()
names = ["Charlie", "Alice", "Bob"]
names.sort(key=lambda name: len(name))  # sort by length
print(names)    # ['Bob', 'Alice', 'Charlie']

# ============================================================
# Docstrings (document your functions!)
# ============================================================
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
help(celsius_to_fahrenheit)        # shows the docstring
