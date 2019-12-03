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

# Create GUI
class TestGUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.guiWindow = None

    @classmethod
    def tearDownClass(cls):
        cls.guiWindow = None

# Create a stack
class TestStacker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.CPU = Computer()

    def step1_test_cpu_creation(self):
        self.assertIsInstance(self.CPU, Computer, msg="Object is not a computer instance")
        
    def step2_test_register_loading(self):
        print("------- Loading EBP with Value 23 ---------")
        self.CPU.load_register("EBP", "23")
        self.assertRegex(self.CPU.registers.view_registers(), "EBP -> 23", msg=t_r("EBP Did not update", "fail"))
        print(t_r(self.CPU.view_registers(), "success"))
        print("------- Loading ESP with Value 34 ---------")
        self.CPU.load_register("ESP", "34")
        self.assertRegex(self.CPU.registers.view_registers(), "ESP -> 34", msg=t_r("ESP Did not update", "fail"))
        print(t_r(self.CPU.view_registers(), "success"))

    def step3_test_stack_creation(self):
        print("Stack was created")
        self.assertIsNot(self.CPU.stack, Stack, msg=t_r("Object is not a stack instance", "fail"))
        print(t_r(self.CPU.view_stack(), "success"))

    def step4_test_stack_push(self):
        print("Pushing 'test' to Stack")
        self.CPU.push_to_stack("test")
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), (["test"], 4), msg=t_r("Failed to Push Item to Stack", "fail"))
        print(t_r(self.CPU.view_stack(), "success"))
        
    def step5_test_stack_pop(self):
        print("Popping 'test' from Stack")
        self.CPU.pop_from_stack()
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), ([], 0), msg=t_r("Failed to Pop item off stack", "fail"))
        print(t_r(self.CPU.view_stack(), "success"))

    def step6_test_register_stack_communication(self):
        print("------- Testing Communication between Stack and Registers -------")
        print("Pushing 'test' to stack")
        self.CPU.stack.push("test")
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), (["test"], 4), msg=t_r("Failed to Push Item to Stack", "fail"))
        print(t_r(self.CPU.view_stack(), "success"))
        print("Popping 'test' into EBP")
        self.CPU.pop_from_stack("EBP")
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), ([], 0), msg=t_r("Failed to Push Item to Stack", "fail"))
        self.assertRegex(self.CPU.registers.view_registers(), "EBP -> test", msg=t_r("ESP Did not update", "fail"))
        print(t_r(self.CPU.view_registers(), "success"))
        print("Pushing ESP (value: 34) onto the stack")
        self.CPU.push_to_stack("ESP")
        self.assertEqual((self.CPU.stack.items, self.CPU.stack.size), (["34"], 4), msg=t_r("Failed to Push Item to Stack", "fail"))
        print(t_r(self.CPU.view_stack(), "success"))
        

    @classmethod
    def tearDownClass(cls):
        cls.CPU = None
if __name__ == '__main__':
    new_runner = unittest.TestLoader()
    new_runner.testMethodPrefix = "step"
    new_runner.loadTestsFromModule(TestStacker)
    unittest.main(verbosity=0, testLoader=new_runner)