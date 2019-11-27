class Stack:
    def __init__(self):
        self.size = 0
        self.items = []
    def push(self, item):
        self.size += 4
        self.items.append(item)
    def pop(self):
        item = self.items.pop()
        self.size -= 4
        return item
    def display_stack(self):
        return("""
            Stack Information: {0},
            Stack Size: {1},
            Stack Items: {2}
            """
            .format(self, self.size, self.items)
            )
