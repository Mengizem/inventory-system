from dataclasses import dataclass


@dataclass
class InventoryItem:
    id: int
    name: str
    unit_price: float
    quantity_on_hand: int = 0
