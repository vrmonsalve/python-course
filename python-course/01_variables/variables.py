# ============================================================
# Module 01 — Variables & Data Types
# ============================================================

# --- String (text) ---
name = "Maria"
city = "New York"

# --- Integer (whole number) ---
age = 25
year = 2024

# --- Float (decimal number) ---
price = 19.99
temperature = 36.6

# --- Boolean (True or False) ---
is_logged_in = True
has_discount = False

# --- Printing variables ---
print("Name:", name)
print("Age:", age)
print("Price: $", price)
print("Logged in:", is_logged_in)

# --- Checking types ---
print("\nData types:")
print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(price))        # <class 'float'>
print(type(is_logged_in)) # <class 'bool'>

# --- String operations ---
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
print("\nFull name:", full_name)
print("Name length:", len(full_name))
print("Uppercase:", full_name.upper())

# --- Number operations ---
a = 10
b = 3
print("\nAddition:", a + b)       # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Integer division:", a // b) # 3
print("Remainder:", a % b)       # 1
print("Power:", a ** b)          # 1000

# --- User input ---
# Uncomment the lines below to try interactive input
# user_name = input("What is your name? ")
# print("Hello,", user_name)

# --- F-strings (formatted strings) ---
product = "laptop"
cost = 999.99
print(f"\nThe {product} costs ${cost:.2f}")
# Output: The laptop costs $999.99
