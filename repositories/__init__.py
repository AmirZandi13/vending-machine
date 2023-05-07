import os


if os.environ.get("STORE") == "mysql":
    from repositories.mysql.machine_repository import MachineRepository
    from repositories.mysql.product_repository import ProductRepository
    from repositories.mysql.order_repository import OrderRepository
elif os.environ.get("STORE") == "postgresql":
    from repositories.postgresql.machine_repository import MachineRepository
    from repositories.postgresql.product_repository import ProductRepository
    from repositories.postgresql.order_repository import OrderRepository
else:
    from repositories.in_memory.machine_repository import MachineRepository
    from repositories.in_memory.product_repository import ProductRepository
    from repositories.in_memory.order_repository import OrderRepository
