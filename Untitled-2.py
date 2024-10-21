#ejemplo de polimorfismo

class Perro():
    def __init__(self, nombre):
        self.nombre = nombre
    def habla(self):
        return self.nombre + " dice guau"
    
class Gato():
    def __init__(self, nombre):
        self.nombre = nombre
    def habla(self):
        return self.nombre + " dice miau"
    
def escuchar(animal):
    print(animal.habla())
    
miperro = Perro("Rex")
migato = Gato("Misifu")

escuchar(miperro)
escuchar(migato)

# Output: Rex dice guau
#         Misifu dice miau
```