"""Task 3: Fee calculator using functions, map/filter/reduce."""

from functools import reduce


def calculate_commission(amount):
    """Return a tiered commission for an order amount."""
    if amount <= 200:
        return amount * 0.10
    elif amount <= 500:
        return amount * 0.15
    else:
        return amount * 0.20


records = [
    {"id": 1, "name": "Swiggy Bites", "amount": 150.00},
    {"id": 2, "name": "Pizza Palace", "amount": 250.00},
    {"id": 3, "name": "Burger Hub", "amount": 375.00},
    {"id": 4, "name": "Spice Route", "amount": 500.00},
    {"id": 5, "name": "Tasty Meals", "amount": 650.00},
    {"id": 6, "name": "Fresh Bowl", "amount": 900.00},
]

# map() + lambda reuses the named calculation for every record.
records_with_fee = list(
    map(
        lambda record: {**record, "fee": calculate_commission(record["amount"])},
        records,
    )
)

print("ALL RECORDS WITH COMMISSION")
print("-" * 50)
for record in records_with_fee:
    print(
        f"ID={record['id']} | {record['name']:<15} | "
        f"Amount=Rs {record['amount']:.2f} | Fee=Rs {record['fee']:.2f}"
    )

threshold = 80.00
audit_records = list(
    filter(lambda record: record["fee"] > threshold, records_with_fee)
)

print(f"\nAUDIT RECORDS: commission > Rs {threshold:.2f}")
print("-" * 50)
for record in audit_records:
    print(f"ID={record['id']} | {record['name']} | Fee=Rs {record['fee']:.2f}")

total_fee = reduce(
    lambda total, record: total + record["fee"],
    records_with_fee,
    0.0,
)

print(f"\nTotal fee: Rs {total_fee:.2f}")
