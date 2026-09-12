"""Mini Capstone: Food Delivery Live Data Pipeline - Console Tool."""

import json
from functools import reduce
from pathlib import Path

import requests


API_URL = "https://jsonplaceholder.typicode.com/posts?_limit=10"
OUTPUT_FILE = Path("data/processed/records.json")


class Order:
    """Represents one restaurant/order record kept in memory."""

    def __init__(self, order_id, name, amount=0.0, status=False):
        self.order_id = order_id
        self.name = name
        self.amount = float(amount)
        self.status = bool(status)

    def to_dict(self):
        return {
            "id": self.order_id,
            "name": self.name,
            "amount": self.amount,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data.get("amount", 0.0),
            data.get("status", False),
        )

    def __repr__(self):
        return (
            f"Order(id={self.order_id!r}, name={self.name!r}, "
            f"amount={self.amount:.2f}, status={self.status})"
        )


def commission(amount):
    if amount <= 200:
        return amount * 0.10
    elif amount <= 500:
        return amount * 0.15
    return amount * 0.20


def fetch_mock_restaurants():
    """Fetch mock restaurants and return Order objects; never crash on API failure."""
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code != 200:
            print(
                f"API error: HTTP {response.status_code}. "
                "Fetch skipped gracefully."
            )
            return []

        payload = response.json()
        records = [
            Order(item["id"], item["title"], 0.0, False)
            for item in payload
        ]

        print("\nTOP 10 MOCK RESTAURANTS")
        print("-" * 50)
        for record in records:
            print(f"{record.order_id:>2} | {record.name}")
        return records

    except requests.RequestException as exc:
        print(f"Network error: {exc}. Fetch skipped gracefully.")
        return []
    except (ValueError, KeyError) as exc:
        print(f"Invalid API response: {exc}. Fetch skipped gracefully.")
        return []


def add_restaurant(records):
    """Add a new Order with numeric input validation."""
    name = input("Restaurant name: ").strip()
    if not name:
        print("Error: restaurant name cannot be empty.")
        return

    while True:
        raw_id = input("Restaurant ID (integer): ").strip()
        try:
            order_id = int(raw_id)
            break
        except ValueError:
            print("Error: ID must be numeric. Please try again.")

    while True:
        raw_amount = input("Order amount (number): ").strip()
        try:
            amount = float(raw_amount)
            break
        except ValueError:
            print("Error: amount must be numeric. Please try again.")

    records.append(Order(order_id, name, amount, False))
    print("Restaurant added successfully.")


def calculate_and_display_commission(records):
    if not records:
        print("No records available.")
        return

    updated = list(
        map(
            lambda record: {
                "record": record,
                "fee": commission(record.amount),
            },
            records,
        )
    )

    print("\nCOMMISSION REPORT")
    print("-" * 60)
    for item in updated:
        record = item["record"]
        print(
            f"{record.name:<25} Amount=Rs {record.amount:8.2f} "
            f"Fee=Rs {item['fee']:8.2f}"
        )

    audit_threshold = 80.0
    audit = list(filter(lambda item: item["fee"] > audit_threshold, updated))
    total_fee = reduce(
        lambda total, item: total + item["fee"],
        updated,
        0.0,
    )

    print(f"\nAudit records (fee > Rs {audit_threshold:.2f}):")
    for item in audit:
        print(f"- {item['record'].name}: Rs {item['fee']:.2f}")

    print(f"Total commission: Rs {total_fee:.2f}")


def save_records(records):
    try:
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump([record.to_dict() for record in records], file, indent=2)
        print(f"Saved {len(records)} records to {OUTPUT_FILE}")
    except Exception as exc:
        print(f"Save error: {exc}")
    finally:
        print("Operation complete")


def load_records(records):
    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
            payload = json.load(file)
        records.clear()
        records.extend(Order.from_dict(item) for item in payload)
        print(f"Loaded {len(records)} records from {OUTPUT_FILE}")
    except FileNotFoundError:
        print("No saved records found; keeping current in-memory records.")
    except Exception as exc:
        print(f"Load error: {exc}")
    finally:
        print("Operation complete")


def save_and_load(records):
    save_records(records)
    load_records(records)


def print_menu():
    print("\n" + "=" * 55)
    print("FOOD DELIVERY LIVE DATA PIPELINE")
    print("=" * 55)
    print("1. Fetch and display top 10 mock restaurants")
    print("2. Add a new restaurant")
    print("3. Calculate and display commission")
    print("4. Save records and load them back")
    print("5. Exit")


def main():
    records = []

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            fetched = fetch_mock_restaurants()
            if fetched:
                records.extend(fetched)
        elif choice == "2":
            add_restaurant(records)
        elif choice == "3":
            calculate_and_display_commission(records)
        elif choice == "4":
            save_and_load(records)
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
