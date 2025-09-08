# Musical Instruments

owner = "Trinidad"
year = 1956

menu = [
    {"name": "Ukelele", "price": 300},
    {"name": "Piano", "price": 1500},
    {"name": "Drums", "price": 2000},
    {"name": "Basketballs/Volleyballs/Badmintons", "price": 450},
    {"name": "Electric Guitar", "price": 300},
]

print("Musical Instruments")
print(f"Owner: {owner}")
print(f"Since {year}\n")
print("-" * 40)
print(f"{'Product Name':<40} {'Price (₱)':>10}")
print("-" * 40)

for item in menu:
    print(f"{item['name']:<40} ₱{item['price']:>7.2f}")

print("-" * 40)
print("Open: 7:00 AM – 8:00 PM")
print("Pre-Order Available")
