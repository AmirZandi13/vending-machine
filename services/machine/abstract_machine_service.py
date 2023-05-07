from abc import ABC, abstractmethod


class AbstractMachineService(ABC):
    @abstractmethod
    def get_machine_by_name(self, name: str) -> dict:
        pass

    @abstractmethod
    def machine_is_available(self, name: str, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def change_state(self, machine_id: int, state: str, machines: list) -> bool:
        pass
