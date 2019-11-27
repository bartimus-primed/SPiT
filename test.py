import unittest
from Stacker.Computer import Computer
from Stacker.Management.Memory.Stack.Stack import Stack

# Create a stack
class TestStacker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.CPU = Computer()
    def test_cpu(self):
        print(self.CPU)
        self.CPU.registers.view_registers()
        print("------- Loading EBP with Value 23 ---------")
        self.CPU.load_register("EBP", "23")
        self.CPU.registers.view_registers()
        self.CPU.load_register("ESP", "34")
        print("------- Loading ESP with Value 34 ---------")
        self.CPU.registers.view_registers()

    def test_stack(self):
        self.assertIsInstance(self.CPU.stack, Stack, msg="Item is not a stack instance")
        self.CPU.stack.display_stack()
        self.CPU.stack.push("test")
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), (["test"], 4), msg="Failed to Push Item to Stack")
        self.CPU.stack.display_stack()
        self.CPU.stack.pop()
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), ([], 0), msg="Failed to Pop item off stack")
        self.CPU.stack.display_stack()
    @classmethod
    def tearDownClass(cls):
        cls.CPU = None
if __name__ == '__main__':
    unittest.main()