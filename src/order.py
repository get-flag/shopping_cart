from __future__ import annotations
from typing import Optional, List, Tuple
from inventory import InventoryManagement

class Order():
    def __init__(self, order_id:str, customer:str, order_date: str, order_items: Optional[List[Tuple[str, int]]]): #order_id, quantity
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.order_items = order_items

    def add_to_order(self, items_to_order:Tuple[str, int]): #pyoduct_id, qty
        self.order_items.append(items_to_order)
        return self.order_items

    def finalize_order(self) -> None:
        for product_id, quantity in self.order_items:
            product = InventoryManagement.get_product(product_id)
            if not product or product.quantity < quantity:
                raise ValueError(f"Product {product_id} is not available!")

        for product_id, quantity in self.order_items:
            product = InventoryManagement.get_product(product_id)
            product.deduct_quantity(quantity)








