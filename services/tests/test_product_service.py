from services.product.v1.product_service import ProductService
from models.product import Product


products_data = Product().products
def test_get_products():
    products = ProductService().get_products(products=products_data)

    result = []
    for product in products_data:
        if product["saleable"]:
            result.append(product)

    assert products == result
