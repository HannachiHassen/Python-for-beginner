# ============================================================
# 03 - Strings in Python
# ============================================================
# A string is a sequence of characters enclosed in quotes.

name = "Alice"
message = 'Hello, World!'
multi_line = """
This string
spans multiple
lines.
"""

# ============================================================
# String Concatenation & Repetition
# ============================================================
first = "Hello"
second = "World"
combined = first + ", " + second + "!"
print(combined)      # Hello, World!
print("ha" * 3)      # hahaha

# ============================================================
# f-Strings (the modern way to format strings)
# ============================================================
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I'll be {age + 1}.")
print(f"Pi is approximately {3.14159:.2f}")  # 2 decimal places

# ============================================================
# Common String Methods
# ============================================================
text = "  Hello, Python!  "

print(text.strip())        # "Hello, Python!"  → remove whitespace
print(text.lower())        # "  hello, python!  "
print(text.upper())        # "  HELLO, PYTHON!  "
print(text.replace("Python", "World"))  # "  Hello, World!  "
print(text.strip().split(", "))         # ['Hello', 'Python!']

sentence = "the quick brown fox"
print(sentence.capitalize())  # "The quick brown fox"
print(sentence.title())       # "The Quick Brown Fox"
print(sentence.count("o"))    # 2
print(sentence.startswith("the"))  # True
print(sentence.endswith("fox"))    # True

# ============================================================
# Indexing & Slicing
# ============================================================
word = "Python"
#        P  y  t  h  o  n
# index: 0  1  2  3  4  5
# neg:  -6 -5 -4 -3 -2 -1

print(word[0])     # P   → first character
print(word[-1])    # n   → last character
print(word[0:3])   # Pyt → slice from index 0 to 2
print(word[2:])    # thon → from index 2 to end
print(word[:4])    # Pyth → from start to index 3
print(word[::-1])  # nohtyP → reversed!

# ============================================================
# Checking String Content
# ============================================================
print("123".isdigit())   # True
print("abc".isalpha())   # True
print("abc123".isalnum())# True
print("  ".isspace())    # True
print("Hello" in "Hello, World!")  # True

# ============================================================
# String Length
# ============================================================
print(len("Hello"))   # 5
print(len(""))        # 0

# ============================================================
# Getting User Input (strings by default)
# ============================================================
# user_name = input("What is your name? ")
# print(f"Nice to meet you, {user_name}!")
