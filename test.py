import unittest
from Stacker.Computer import Computer
from Stacker.Management.Memory.Stack.Stack import Stack

def t_r(item, test_result):
    success = '\033[92m'
    failure = '\033[91m'
    end_line = '\033[0m'
    if test_result == "fail":
        return "{}{}{}".format(failure, item, end_line)
    else:
        return "{}{}{}".format(success, item, end_line)

# Create a stack
class TestStacker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.CPU = Computer()

    def test_cpu_creation(self):
        self.assertIsInstance(self.CPU, Computer, msg="Object is not a computer instance")
        
    def test_register_loading(self):
        print("------- Loading EBP with Value 23 ---------")
        self.CPU.load_register("EBP", "23")
        self.assertRegex(self.CPU.registers.view_registers(), "EBP -> 23", msg=t_r("EBP Did not update", "fail"))
        print(t_r(self.CPU.view_registers(), "success"))
        print("------- Loading ESP with Value 34 ---------")
        self.CPU.load_register("ESP", "34")
        self.assertRegex(self.CPU.registers.view_registers(), "ESP -> 34", msg=t_r("ESP Did not update", "fail"))
        print(t_r(self.CPU.view_registers(), "success"))

    def test_stack_creation(self):
        print("Stack was created")
        self.assertIsNot(self.CPU.stack, Stack, msg=t_r("Object is not a stack instance", "fail"))
        print(t_r(self.CPU.stack.display_stack(), "success"))

    def test_stack_operations(self):
        print("Pushing 'test' to Stack")
        self.CPU.stack.push("test")
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), (["test"], 4), msg=t_r("Failed to Push Item to Stack", "fail"))
        print(t_r(self.CPU.stack.display_stack(), "success"))
        print("Popping 'test' from Stack")
        self.CPU.stack.pop()
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), ([], 0), msg=t_r("Failed to Pop item off stack", "fail"))
        print(t_r(self.CPU.stack.display_stack(), "success"))

    @classmethod
    def tearDownClass(cls):
        cls.CPU = None
if __name__ == '__main__':
    unittest.main(verbosity=0)