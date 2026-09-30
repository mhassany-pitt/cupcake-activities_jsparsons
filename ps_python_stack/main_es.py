def apilar(self, elemento):
    self.items.insert(0, elemento)
def desapilar(self):
    if self.is_empty():
        print("error la pila esta vacia")
    else:
        return self.items.pop(0)
