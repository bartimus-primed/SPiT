from Stacker.Management.Memory.Stack.Stack import Stack
from Stacker.Management.Registers.Registers import Registers
class Computer:
    def __init__(self):
        self.stack = Stack()
        self.registers = Registers()
    def push_to_stack(self, item):
        if self.registers.registers.keys().__contains__(item):
            item = self.registers.registers[item].get_value()
        self.stack.push(item)
    def pop_from_stack(self, register=None):
        item = self.stack.pop()
        if register:
            self.registers.registers[register].set_value(item)
    def load_register(self, register, value):
        self.registers.load_register(register, value)
    def view_registers(self):
        return self.registers.view_registers()
    def view_stack(self):
        return self.stack.display_stack()