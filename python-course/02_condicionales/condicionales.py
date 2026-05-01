# ============================================================
# Module 02 — Conditionals
# ============================================================

# --- Basic if / else ---
age = 20

if age >= 18:
    print("Access granted — you are an adult.")
else:
    print("Access denied — you are a minor.")

# --- if / elif / else ---
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nScore: {score} → Grade: {grade}")

# --- Logical operators: and, or, not ---
has_ticket = True
is_vip = False

if has_ticket and is_vip:
    print("\nVIP entrance — enjoy the show!")
elif has_ticket and not is_vip:
    print("\nRegular entrance — enjoy the show!")
else:
    print("\nNo ticket — access denied.")

# --- Nested conditionals ---
temperature = 30

if temperature > 0:
    if temperature > 25:
        print("\nIt is hot outside. Wear light clothes.")
    else:
        print("\nThe weather is pleasant.")
else:
    print("\nIt is freezing! Stay inside.")

# --- Ternary (one-line conditional) ---
number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"\n{number} is {result}")

# --- Real example: login system ---
print("\n--- Login System ---")
stored_password = "python123"
entered_password = "python123"

if entered_password == stored_password:
    print("Login successful! Welcome back.")
else:
    print("Wrong password. Please try again.")
