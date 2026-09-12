"""Task 4: Class-based record manager with JSON persistence."""

import json
from pathlib import Path


class Order:
    def __init__(
        self,
        order_id,
        restaurant_name,
        amount,
        delivery_time_minutes,
        is_delivered,
    ):
        self.order_id = order_id
        self.restaurant_name = restaurant_name
        self.amount = float(amount)
        self.delivery_time_minutes = int(delivery_time_minutes)
        self.is_delivered = bool(is_delivered)

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "restaurant_name": self.restaurant_name,
            "amount": self.amount,
            "delivery_time_minutes": self.delivery_time_minutes,
            "is_delivered": self.is_delivered,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["order_id"],
            data["restaurant_name"],
            data["amount"],
            data["delivery_time_minutes"],
            data["is_delivered"],
        )

    def __repr__(self):
        return (
            f"Order(order_id={self.order_id!r}, "
            f"restaurant_name={self.restaurant_name!r}, "
            f"amount={self.amount!r}, "
            f"delivery_time_minutes={self.delivery_time_minutes!r}, "
            f"is_delivered={self.is_delivered!r})"
        )


def save_records(records, filepath):
    try:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump([record.to_dict() for record in records], file, indent=2)
        print(f"Saved {len(records)} records to {filepath}")
    except Exception as exc:
        print(f"Save error: {exc}")
    finally:
        print("Operation complete")


def load_records(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        records = [Order.from_dict(item) for item in data]
        print(f"Loaded {len(records)} records from {filepath}")
        return records
    except FileNotFoundError:
        print(f"File not found: {filepath}; returning an empty list")
        return []
    except Exception as exc:
        print(f"Load error: {exc}")
        return []
    finally:
        print("Operation complete")


if __name__ == "__main__":
    output_file = "data/processed/records.json"

    records = [
        Order("FD001", "Swiggy Bites", 250.0, 30, True),
        Order("FD002", "Pizza Palace", 520.5, 42, False),
    ]

    save_records(records, output_file)
    loaded_records = load_records(output_file)

    print("\nRECONSTRUCTED OBJECTS")
    for record in loaded_records:
        print(record)
