import sys
sys.path.append("../../")
from repositories.abstract_product_repository import AbstractProductRepository


class ProductRepository(AbstractProductRepository):
    def get_products(self, *args, **kwargs) -> list:
        products = kwargs.get("products")

        result = []
        for product in products:
            if product["saleable"]:
                result.append(product)

        return result
