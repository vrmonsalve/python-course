# ============================================================
# Module 03 — Loops
# ============================================================

# --- for loop with range ---
print("--- Counting with range ---")
for i in range(1, 6):
    print(f"Number: {i}")

# --- for loop over a list ---
print("\n--- Looping over a list ---")
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# --- for loop with index using enumerate ---
print("\n--- With index (enumerate) ---")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# --- while loop ---
print("\n--- while loop ---")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# --- break — exit the loop early ---
print("\n--- break example ---")
for number in range(10):
    if number == 5:
        print("Found 5! Stopping.")
        break
    print(number)

# --- continue — skip an iteration ---
print("\n--- continue example (skip even numbers) ---")
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)

# --- Nested loops ---
print("\n--- Multiplication table (1 to 3) ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()

# --- Real example: calculate total sales ---
print("--- Total Sales ---")
sales = [150.0, 200.5, 99.9, 310.0, 450.75]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total:.2f}")
