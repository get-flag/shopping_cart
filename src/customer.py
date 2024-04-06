from __future__ import annotations
from typing import List,Optional, Set, Tuple


class Customer():
    def __init__(self, customer_id:str, name:str, transactions:Optional[Set[Tuple[str, int, float]]]=None): #transaction = [product_id], price, quantity]
        self.customer_id = customer_id
        self.name = name
        self.transactions = transactions if transactions is not None else set()

    def add_transaction(self, transaction:Tuple[str, int, float]) -> None:
        if transaction in self.transactions:
            raise ValueError("transaction already added")
        self.transactions.add(transaction)

    def search_transaction(self, product_id:str) -> List:
        matching_transactions = []
        for transaction in self.transactions:
            if product_id == transaction[0]:
                matching_transactions.append(transaction)
        if len(matching_transactions) == 0:
            raise ValueError(f"There are no matching transactions for product_id {product_id}!")
        return matching_transactions
        # return [transaction for transaction in self.transactions if product_id==transaction[0]]

