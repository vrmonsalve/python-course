# ============================================================
# Project 01 — Calculator
# ============================================================
# A simple command-line calculator that supports
# addition, subtraction, multiplication, and division.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return "Error: Unknown operator."

def main():
    print("=" * 30)
    print("      🧮 Python Calculator")
    print("=" * 30)
    print("Operators: + - * /")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            entry = input("Enter expression (e.g. 5 + 3): ").strip()

            if entry.lower() == "exit":
                print("Goodbye!")
                break

            parts = entry.split()
            if len(parts) != 3:
                print("Please enter in the format: number operator number\n")
                continue

            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            result = calculate(a, operator, b)

            if isinstance(result, float) and result == int(result):
                print(f"Result: {int(result)}\n")
            else:
                print(f"Result: {result}\n")

        except ValueError:
            print("Please enter valid numbers.\n")

if __name__ == "__main__":
    main()
