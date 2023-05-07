from abc import ABC, abstractmethod


class AbstractOrderRepository(ABC):
    @abstractmethod
    def create_order(self, machine_id: int, product_id: int):
        pass