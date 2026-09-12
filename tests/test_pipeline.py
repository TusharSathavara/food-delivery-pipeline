import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from food_delivery_pipeline import Order, commission


def test_commission_tiers():
    assert commission(200) == 20
    assert commission(201) == 30.15
    assert commission(500) == 75
    assert commission(501) == 100.2


def test_order_serialization():
    order = Order(1, "Test Restaurant", 250, True)
    restored = Order.from_dict(order.to_dict())

    assert restored.order_id == 1
    assert restored.name == "Test Restaurant"
    assert restored.amount == 250.0
    assert restored.status is True
