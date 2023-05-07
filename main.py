import os
from dotenv import load_dotenv
load_dotenv(".env")

from models.machine import Machine
from models.product import Product
from services.machine.v1.machine_service import MachineService
from services.product.v1.product_service import ProductService
from services.order.v1.order_service import OrderService


def vending_machine():
   machines_data = Machine().machines
   products_data = Product().products
   machine_name = os.environ.get("MACHINE")
   machine = MachineService().get_machine_by_name(name=machine_name, machines=machines_data)
   if not machine:
      print(f"machine: {machine_name} does not exist")
      return ""

   machine_is_available = MachineService().machine_is_available(name=machine_name, machines=machines_data)
   if not machine_is_available:
      print(f"machine: {machine_name} is running, please wait")
      return ""

   while True:
      input("type any key to enter the coin:\n")

      machines_data = MachineService().change_state(machine_id=machine.get("id"), state=Machine().RUNNING,
                                                    machines=machines_data)

      products = ProductService().get_products(products=products_data)

      product_input = "Choose a product number from the list:\n"
      for product in products:
         product_input += f"{product.get('id')} - {product.get('name')}\n"

      product_id = int(input(product_input))

      order_output = ""
      for product in products:
         if product.get("id") == product_id:
            order_output += f"{product.get('name')} is delivered"

      if not order_output:
         order_output += "The product number is wrong"

      print(f"\n\n{order_output}\n\n")

      machines_data = MachineService().change_state(machine_id=machine.get("id"), state=Machine().IDLE,
                                                    machines=machines_data)

      OrderService().create_order(machine.get("id"), product_id)


vending_machine()
