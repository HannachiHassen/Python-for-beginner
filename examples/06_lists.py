# ============================================================
# 06 - Lists in Python
# ============================================================
# A list is an ordered, mutable (changeable) collection of items.

# --- Creating a list ---
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", True, 3.14]   # can hold different types
empty = []

# ============================================================
# Accessing Items (Indexing)
# ============================================================
print(fruits[0])    # apple  (first item)
print(fruits[-1])   # cherry (last item)
print(fruits[1:3])  # ['banana', 'cherry'] (slicing)

# ============================================================
# Modifying a List
# ============================================================
fruits[1] = "mango"         # change an item
print(fruits)               # ['apple', 'mango', 'cherry']

fruits.append("grape")      # add to the end
print(fruits)               # ['apple', 'mango', 'cherry', 'grape']

fruits.insert(1, "kiwi")   # insert at position 1
print(fruits)               # ['apple', 'kiwi', 'mango', 'cherry', 'grape']

fruits.remove("mango")      # remove by value
print(fruits)               # ['apple', 'kiwi', 'cherry', 'grape']

popped = fruits.pop()       # remove and return last item
print(popped)               # grape
print(fruits)               # ['apple', 'kiwi', 'cherry']

del fruits[0]               # delete by index
print(fruits)               # ['kiwi', 'cherry']

# ============================================================
# Useful List Methods
# ============================================================
nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(nums))            # 8   → number of items
print(nums.count(1))        # 2   → how many times 1 appears
print(nums.index(9))        # 5   → index of first 9

nums.sort()
print(nums)                 # [1, 1, 2, 3, 4, 5, 6, 9]

nums.reverse()
print(nums)                 # [9, 6, 5, 4, 3, 2, 1, 1]

nums_copy = nums.copy()     # make a copy (not just another reference)

nums.clear()
print(nums)                 # []

# ============================================================
# Combining Lists
# ============================================================
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)                    # [1, 2, 3, 4, 5, 6]
print(a * 3)                # [1, 2, 3, 1, 2, 3, 1, 2, 3]

a.extend(b)                 # adds all items of b to a
print(a)                    # [1, 2, 3, 4, 5, 6]

# ============================================================
# Checking Membership
# ============================================================
colors = ["red", "green", "blue"]
print("red" in colors)      # True
print("yellow" in colors)   # False

# ============================================================
# List Comprehension (elegant shortcut!)
# ============================================================
# Create a new list from an existing one in one line.

squares = [x ** 2 for x in range(1, 6)]
print(squares)              # [1, 4, 9, 16, 25]

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)         # [4, 16, 36, 64, 100]

upper_fruits = [f.upper() for f in ["apple", "banana"]]
print(upper_fruits)         # ['APPLE', 'BANANA']

# ============================================================
# Looping over a List
# ============================================================
animals = ["cat", "dog", "bird"]

for animal in animals:
    print(animal)

for i, animal in enumerate(animals):
    print(f"{i + 1}. {animal}")
