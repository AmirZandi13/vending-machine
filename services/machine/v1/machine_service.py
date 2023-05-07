from dotenv import load_dotenv
load_dotenv("./.env")

from services.machine.abstract_machine_service import AbstractMachineService
from repositories import MachineRepository


class MachineService(AbstractMachineService):
   def get_machine_by_name(self, name: str, *args, **kwargs) -> dict:
      machine = MachineRepository().get_machine_by_name(name=name, machines=kwargs.get("machines"))
      return machine

   def machine_is_available(self, name: str, *args, **kwargs) -> bool:
      machine_is_available = MachineRepository().machine_is_available(name=name, machines=kwargs.get("machines"))
      return machine_is_available

   def change_state(self, machine_id: int, state: str, machines: list) -> list:
      machines = MachineRepository().change_state(machine_id, state, machines)
      return machines

