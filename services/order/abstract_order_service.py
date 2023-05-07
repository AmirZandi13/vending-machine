from abc import ABC, abstractmethod


class AbstractOrderService(ABC):
    @abstractmethod
    def create_order(self, machine_id: int, product_id: int):
        pass
