# ============================================================
# Module 05 — Data Structures
# ============================================================

# ============================================================
# LISTS — ordered, mutable, allows duplicates
# ============================================================
print("=== LISTS ===")
fruits = ["apple", "banana", "cherry"]

# Access by index
print(fruits[0])       # apple
print(fruits[-1])      # cherry (last item)

# Modify
fruits.append("mango")        # add to end
fruits.insert(1, "grape")     # add at position
fruits.remove("banana")       # remove by value
popped = fruits.pop()         # remove and return last item

print(fruits)
print(f"Popped: {popped}")
print(f"Length: {len(fruits)}")

# Loop through list
for fruit in fruits:
    print(f"  - {fruit}")

# List comprehension (create list in one line)
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(f"\nSquares: {squares}")

evens = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")


# ============================================================
# TUPLES — ordered, immutable
# ============================================================
print("\n=== TUPLES ===")
coordinates = (40.7128, -74.0060)   # New York City
rgb_red = (255, 0, 0)

print(f"Latitude: {coordinates[0]}")
print(f"Longitude: {coordinates[1]}")
print(f"Red color: {rgb_red}")

# Unpacking
lat, lon = coordinates
print(f"Unpacked: lat={lat}, lon={lon}")


# ============================================================
# DICTIONARIES — key-value pairs
# ============================================================
print("\n=== DICTIONARIES ===")
user = {
    "name": "Maria",
    "age": 25,
    "email": "maria@example.com",
    "is_active": True
}

# Access values
print(user["name"])
print(user.get("phone", "No phone"))  # safe access with default

# Modify
user["age"] = 26
user["city"] = "New York"

# Loop
for key, value in user.items():
    print(f"  {key}: {value}")

# Check if key exists
if "email" in user:
    print(f"\nEmail found: {user['email']}")


# ============================================================
# SETS — unique values, unordered
# ============================================================
print("\n=== SETS ===")
tags = {"python", "programming", "beginner", "python"}  # duplicate removed
print(tags)

tags.add("coding")
tags.discard("beginner")
print(tags)

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nUnion: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference: {set_a - set_b}")
