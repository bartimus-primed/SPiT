class Stack:
    def __init__(self):
        self.size = 0
        self.items = []
    def push(self, item):
        self.size += 4
        self.items.append(item)
        return None
    def pop(self, register=None):
        print(self.items)
        item = self.items.pop()
        if register:
            register.set_value(item)
        self.size -= 4
    def display_stack(self):
        print("""
            Stack Information: {0},
            Stack Size: {1},
            Stack Items: {2}
            """
            .format(self, self.size, self.items)
            )
