from repositories import MachineRepository
from models.machine import Machine


machines = Machine().machines
def test_get_machine_by_name_when_machine_exists():
    machine_name = "machine-1"
    machine = MachineRepository().get_machine_by_name(machine_name, machines=machines)

    assert machine != {}


def test_get_machine_by_name_when_machine_does_not_exists():
    machine_name = "machine-1"
    machine = MachineRepository().get_machine_by_name(machine_name, machines=machines)

    assert machine == {
        "id": 1,
        "name": "machine-1",
        "state": Machine().IDLE,
    }


def test_machine_is_available_when_machine_is_in_idle_state():
    machine_name = "machine-1"
    machine_is_available = MachineRepository().machine_is_available(machine_name, machines=machines)

    assert machine_is_available == True


def test_machine_is_available_when_machine_is_not_in_idle_state():
    machine_name = "machine-1"
    machines_data = [
        {
            "id": 1,
            "name": "machine-1",
            "state": Machine().RUNNING,
        }
    ]
    machine_is_available = MachineRepository().machine_is_available(machine_name, machines=machines_data)

    assert machine_is_available == False


def test_change_state_of_machine():
    machines_data = [
        {
            "id": 1,
            "name": "machine-1",
            "state": Machine().IDLE,
        }
    ]

    machines_data_after_change_the_state = MachineRepository().change_state(machines_data[0]["id"], Machine().RUNNING,
                                                                            machines_data)

    assert machines_data_after_change_the_state[0]["state"] == Machine().RUNNING

