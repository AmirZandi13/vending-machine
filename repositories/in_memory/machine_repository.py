import sys
sys.path.append("../../")
from repositories.abstract_machine_repository import AbstractMachineRepository
from models.machine import Machine

class MachineRepository(AbstractMachineRepository):
    def get_machine_by_name(self, name: str, *args, **kwargs) -> dict:
        machines = kwargs.get("machines")

        if not machines:
            return {}

        for machine in machines:
            if machine["name"] == name:
                return machine

        return {}

    def machine_is_available(self, name: str, *args, **kwargs) -> bool:
        machines = kwargs.get("machines")

        if not machines:
            return False

        for machine in machines:
            if (machine["name"] == name) and (machine["state"] == Machine().IDLE):
                return True

        return False

    def change_state(self, machine_id: int, state: str, machines: list) -> list:
        for index, machine in enumerate(machines):
            if machine.get("id") == machine_id:
                machines[index]["state"] = state

        return machines
