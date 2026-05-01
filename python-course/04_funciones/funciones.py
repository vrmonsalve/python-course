# ============================================================
# Module 04 — Functions
# ============================================================

# --- Basic function ---
def greet():
    print("Hello, World!")

greet()

# --- Function with parameters ---
def greet_user(name):
    print(f"Hello, {name}! Welcome.")

greet_user("Maria")
greet_user("Carlos")

# --- Function with return value ---
def add(a, b):
    return a + b

result = add(5, 3)
print(f"\n5 + 3 = {result}")

# --- Function with default parameter ---
def power(base, exponent=2):
    return base ** exponent

print(f"\n3 squared: {power(3)}")       # uses default exponent=2
print(f"2 cubed: {power(2, 3)}")        # uses exponent=3

# --- Function with multiple return values ---
def min_max(numbers):
    return min(numbers), max(numbers)

data = [4, 2, 9, 1, 7]
minimum, maximum = min_max(data)
print(f"\nMin: {minimum}, Max: {maximum}")

# --- Real example: calculate total with tax ---
def calculate_total(price, tax_rate=0.19):
    tax = price * tax_rate
    total = price + tax
    return total

subtotal = 100.0
total = calculate_total(subtotal)
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Total with 19% tax: ${total:.2f}")

# --- Real example: validate email ---
def is_valid_email(email):
    return "@" in email and "." in email

emails = ["user@example.com", "invalid-email", "test@domain.org"]
print("\n--- Email Validation ---")
for email in emails:
    status = "valid" if is_valid_email(email) else "invalid"
    print(f"{email} → {status}")

# --- Recursive function: factorial ---
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"\n5! = {factorial(5)}")   # 120
print(f"10! = {factorial(10)}")  # 3628800
