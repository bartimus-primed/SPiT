from Stacker.Management.Memory.Stack.Stack import Stack
from Stacker.Management.Registers.Registers import Registers
class Computer:
    def __init__(self):
        self.stack = Stack()
        self.registers = Registers()
    def push(self, item):
        self.stack.push(item)
    def pop(self, register=None):
        self.stack.pop(self.registers.registers["ebp"])
    def load_register(self, register, value):
        self.registers.load_register(register, value)