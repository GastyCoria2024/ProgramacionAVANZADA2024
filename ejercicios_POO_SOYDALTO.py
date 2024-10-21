#class estudiante :
    #def __init__(self, nombre, edad,grado):
        #self.nombre = nombre
        #self.edad = edad
        #self.grado = grado
    
    #nombre=input("Ingrese el nombre del estudiante: ")
    #edad=input("Ingrese la edad del estudiante: ")
    #grado=input("Ingrese el grado del estudiante: ")

#print(f"Nombre: {estudiante.edad}")

class animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

        def comer(self):
            print("El animal esta comiendo")
    
    def __str__(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}, especie: {self.especie}"
    
    class mamifero:
        def __init__(self, gestacion, lactancia):
            self.gestacion = gestacion
            self.lactancia = lactancia

            def amantar(self):
                print("El mamifero esta amantando")

            def __str__(self):
                return f"Gestacion: {self.gestacion}, lactancia: {self.lactancia}"
        
    class ave:
            def __init__(self, vuelo):
                self.vuelo = vuelo

            def volar(self):
                print("El ave esta volando")

            def __str__(self):
                return f"Vuelo: {self.vuelo}"
            

    class Murcielago(mamifero,ave):
        def __init__(self, nombre, edad, especie, gestacion, lactancia, vuelo):
            super().__init__(nombre, edad, especie, gestacion, lactancia)
            self.vuelo = vuelo

            def volar(self):
                print("El murcielago esta volando")

            def __str__(self):
                return f"{super().__str__()}, vuelo: {self.vuelo}"


    murcielago1 = Murcielago("Murcielago", 2, "murcielago", 6, 3, "si")

    print(murcielago1)


            
           