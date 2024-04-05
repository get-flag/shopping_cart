from __future__ import annotations
from typing import List, Optional, Union

class Product():
    def __init__(self, product_id : str, name: str,description: str, price: float, quantity_available: int):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity_available

    def restock(self,quantity_to_restock: int) -> int:
        if quantity_to_restock < 1:
            raise ValueError("Quantity to restock must be positive")
        self.quantity +=quantity_to_restock
        return self.quantity

    def deduct_quantity(self, quantity_to_deduct:int) -> int:
        if self.quantity - quantity_to_deduct < 0:
            raise OverflowError("Trying to deduct more quantity than existing")
        self.quantity -= quantity_to_deduct
        return self.quantity
