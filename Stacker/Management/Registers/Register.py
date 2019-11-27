from enum import Enum, auto


class Register(Enum):
    EIP = auto()
    EBP = auto()
    ESP = auto()
    EAX = auto()
    EBX = auto()
    ECX = auto()
    EDX = auto()
    ESI = auto()
    EDI = auto()
    def __init__(self, register_value=None):
        self.register_value = register_value
    def get_value(self):
        return self.register_value
    def set_value(self, register_value=""):
        self.register_value = register_value
