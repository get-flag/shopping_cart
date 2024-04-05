from __future__ import annotations
from typing import Optional, Dict
from product import Product

class InventoryManagement():
    products: Dict[str,Product] = {}

    @classmethod
    def add_product(cls, product:Product) -> None:
        """
        Add product
        :type product: object
        """
        if product.product_id in cls.products:
            raise ValueError("Product already exists")
        cls.products[product.product_id] = product

    @classmethod
    def removing_product(cls, product:Product) -> None:
        """
        Remove product
        :param product:
        :return:
        """
        if product.product_id not in cls.products:
            raise ValueError("Product doesn't exist")
        del cls.products[product.product_id]

    @classmethod
    def update_product(cls, product:Product) ->None:
        """
        Update product
        :param product:
        :return:
        """
        if not product.product_id in cls.products:
            raise ValueError("Product doesn't exist to update")
        cls.products[product.product_id] = product

    @classmethod
    def display_all_products(cls) -> dict:
        """
        Display all products
        :return:
        """
        return cls.products


