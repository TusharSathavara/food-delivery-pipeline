"""Task 2: Clean and validate a hardcoded list of restaurant records."""

raw_restaurants = [
    "  swiggy bites  ",
    "ZOMATO KITCHEN",
    "pizza palace",
    "  burger HUB",
    "",
    "12345",
    "  spice route  ",
    "Tasty Meals",
    "   ",
    "fresh bowl",
]

amount_strings = [
    "Rs 150",
    "200.50",
    "Rs 325.75",
    "410",
    "Rs 99.99",
    "275.25",
    "Rs 500",
    "125.50",
    "Rs 80",
    "Rs 220",
]

valid_restaurants = []
skipped = 0

print("CLEANING RESTAURANT RECORDS")
print("-" * 35)

for raw_name in raw_restaurants:
    cleaned = raw_name.strip()

    if not cleaned:
        print("Skipped: empty entry")
        skipped += 1
        continue

    if cleaned.isnumeric():
        print(f"Skipped: numeric-only entry -> {cleaned}")
        skipped += 1
        continue

    cleaned = cleaned.replace("  ", " ")
    cleaned = cleaned.title()
    valid_restaurants.append(cleaned)
    print(f"Valid: {cleaned}")

running_total = 0.0
print("\nAMOUNT RUNNING TOTAL")
print("-" * 35)

for amount_text in amount_strings:
    numeric_text = amount_text.strip().replace("Rs", "").strip()
    amount = float(numeric_text)
    running_total += amount
    print(f"{amount:8.2f} -> running total: {running_total:8.2f}")

print("\nSUMMARY")
print("-" * 35)
print(f"Total valid records : {len(valid_restaurants)}")
print(f"Total skipped       : {skipped}")
print(f"Running total amount: Rs {running_total:.2f}")
