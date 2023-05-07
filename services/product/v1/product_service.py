from dotenv import load_dotenv
load_dotenv("./.env")

from services.product.abstract_product_service import AbstractProductService

from repositories import ProductRepository


class ProductService(AbstractProductService):
   def get_products(self, *args, **kwargs) -> list:
      products = ProductRepository().get_products(products=kwargs.get("products"))

      return products