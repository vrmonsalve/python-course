# ⚙️ Module 04 — Functions

## What is a Function?

A function is a **reusable block of code** that performs a specific task. Instead of writing the same code multiple times, you define it once and call it whenever you need it.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Maria")   # Hello, Maria!
greet("Carlos")  # Hello, Carlos!
```

---

## Anatomy of a Function

```python
def function_name(parameter1, parameter2):
    # code here
    return result
```

- `def` — keyword to define a function
- `parameters` — inputs the function receives
- `return` — the output the function sends back

---

## Real Life Uses

- **Validation** — a function that checks if an email is valid
- **Calculation** — a function that computes tax on a price
- **Formatting** — a function that formats a date
- Every time you call `print()` or `len()`, you are using a built-in function

---

## How to Run

```bash
python funciones.py
```
