def push(self, item):
    self.items.insert(0, item)
def pop(self):
    if self.is_empty():
        print("error stack is empty")
    else:
        return self.items.pop(0)
