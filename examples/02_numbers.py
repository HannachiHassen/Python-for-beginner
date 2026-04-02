# ============================================================
# 02 - Numbers in Python
# ============================================================

# --- Types of numbers ---
whole = 42          # int
decimal = 3.14      # float
big = 1_000_000     # underscores help readability

print(type(whole))    # <class 'int'>
print(type(decimal))  # <class 'float'>

# ============================================================
# Basic Arithmetic
# ============================================================
a = 10
b = 3

print(a + b)   # 13  → Addition
print(a - b)   # 7   → Subtraction
print(a * b)   # 30  → Multiplication
print(a / b)   # 3.333... → Division (always returns float)
print(a // b)  # 3   → Floor division (drops the decimal)
print(a % b)   # 1   → Modulus (remainder)
print(a ** b)  # 1000 → Exponentiation (10 to the power of 3)

# ============================================================
# Useful Built-in Functions
# ============================================================
print(abs(-7))          # 7   → Absolute value
print(round(3.7))       # 4   → Round to nearest int
print(round(3.14159, 2))# 3.14 → Round to 2 decimal places
print(max(1, 5, 3))     # 5   → Largest value
print(min(1, 5, 3))     # 1   → Smallest value
print(sum([1, 2, 3, 4]))# 10  → Sum of a list

# ============================================================
# The math Module (extra power!)
# ============================================================
import math

print(math.sqrt(16))    # 4.0   → Square root
print(math.pi)          # 3.14159...
print(math.floor(3.9))  # 3     → Round down
print(math.ceil(3.1))   # 4     → Round up
print(math.factorial(5))# 120   → 5! = 5×4×3×2×1

# ============================================================
# Type Conversion
# ============================================================
x = 5
y = 2.0

# int + float → float (Python promotes automatically)
print(x + y)       # 7.0

# Force conversion
print(int(2.9))    # 2   (truncates, does NOT round)
print(float(5))    # 5.0
print(str(42))     # "42" (number → string)
print(int("100"))  # 100  (string → int)

# ============================================================
# Augmented Assignment Shortcuts
# ============================================================
score = 0
score += 10    # same as: score = score + 10
score -= 3     # same as: score = score - 3
score *= 2     # same as: score = score * 2
print(score)   # 14
