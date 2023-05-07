import sys
sys.path.append("../../")
from repositories.abstract_order_repository import AbstractOrderRepository


class OrderRepository(AbstractOrderRepository):
    def create_order(self, machine_id: int, product_id: int) -> list:
        # Here we should create an order
        pass
