from dotenv import load_dotenv
load_dotenv("./.env")

from services.order.abstract_order_service import AbstractOrderService

from repositories import OrderRepository


class OrderService(AbstractOrderService):
    def create_order(self, machine_id: int, product_id: int):
        OrderRepository().create_order(machine_id, product_id)
