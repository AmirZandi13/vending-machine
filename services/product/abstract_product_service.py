from abc import ABC, abstractmethod


class AbstractProductService(ABC):
    @abstractmethod
    def get_products(self, *args, **kwargs) -> list:
        pass
