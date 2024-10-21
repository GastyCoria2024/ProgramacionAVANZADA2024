#class Empuje :
    #def __init__(self, press_de_banca, press_militar, press_frances):
        #self.press_de_banca = press_de_banca
        #self.press_militar = press_militar
        #self.press_frances = press_frances

    #def Pecho(self):
        #print(f"Cuando se realiza {self.press_de_banca} se ejercita el pectoral.")

    #def Hombros(self):
        #print(f"Cuando se realiza {self.press_militar} se ejercita hombros")

    #def Triceps(self):
        #print(f"Cuando se realiza {self.press_frances} se ejercita el triceps")

 #Crear una instancia de la clase Empuje
#mi_ejercicio = Empuje("Press de banca", "Press militar", "Press frances")

 #Acceder a los atributos de la instancia
#print(f"Press de banca: {mi_ejercicio.press_de_banca}")

#print(f"Press militar: {mi_ejercicio.press_militar}")

#print(f"Press frances: {mi_ejercicio.press_frances}")

#Llamar a los métodos de la instancia

#mi_ejercicio.Pecho()
#mi_ejercicio.Hombros()
#mi_ejercicio.Triceps()#

#agregar clase tiron con sus metodos y atributos
#class Tiron:
    #def __init__(self, dominadas, remo_con_mancuerna,pull_over_en_polea, curl_inclinado):
        #self.dominadas = dominadas
        #self.remo_con_mancuerna = remo_con_mancuerna
        #self.pull_over_en_polea = pull_over_en_polea
        #self.curl_inclinado = curl_inclinado

    #def Espalda(self):
        #print(f"Cuando se realiza {self.dominadas} se ejercita la espalda.")

    #def Espalda2(self):
        #print(f"Cuando se realiza {self.remo_con_mancuerna} se ejercita espalda")

    #def Espalda3(self):
        #print(f"Cuando se realiza {self.pull_over_en_polea} se ejercita la espalda")

    #def Biceps(self):
        #print(f"Cuando se realiza {self.curl_inclinado} se ejercita el biceps")

# Crear una instancia de la clase Tiron
#mi_ejercicio = Tiron("Dominadas", "remo_con_mancuerna", "pull_over_en_polea" , "curl_inclinado")

# Acceder a los atributos de la instancia
#print(f"Dominadas: {mi_ejercicio.dominadas}")

#print(f"Remo: {mi_ejercicio.remo_con_mancuerna}")

#print(f"Curl: {mi_ejercicio.curl_inclinado}")

#print(f"Pull over: {mi_ejercicio.pull_over_en_polea}")

#necesito ejemplos de programacion orientada a objetos con herencia

# Path: Untitled-1.py

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

class Gato(Animal):

    def maullar(self):
        print(f"{self.nombre} está maullando.")

# Crear una instancia de la clase Perro

mi_perro = Perro("Firulais", 5, "Labrador")

# Acceder a los atributos de la instancia
print(f"Nombre: {mi_perro.nombre}")
print(f"Edad: {mi_perro.edad}")
print(f"Raza: {mi_perro.raza}")

# Llamar a los métodos de la instancia
mi_perro.comer()
mi_perro.dormir()
mi_perro.ladrar()

# Crear una instancia de la clase Gato
mi_gato = Gato("Garfield", 3)

# Acceder a los atributos de la instancia
print(f"Nombre: {mi_gato.nombre}")
print(f"Edad: {mi_gato.edad}")

# Llamar a los métodos de la instancia
mi_gato.comer()
mi_gato.dormir()
mi_gato.maullar()

# Path: Untitled-1.py

#hacer el mismo codigo pero con herencia multiple

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def jugar(self):
        print(f"{self.nombre} está jugando.")

class Perro(Animal, Mascota):
    def __init__(self, nombre, edad, raza):
        Animal.__init__(self, nombre, edad)
        Mascota.__init__(self, nombre, edad)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

class Gato(Animal, Mascota):
    
        def maullar(self):
            print(f"{self.nombre} está maullando.")

# Crear una instancia de la clase Perro
mi_perro = Perro("Firulais", 5, "Labrador")

# Acceder a los atributos de la instancia
print(f"Nombre: {mi_perro.nombre}")
print(f"Edad: {mi_perro.edad}")
print(f"Raza: {mi_perro.raza}")

# Llamar a los métodos de la instancia
mi_perro.comer()
mi_perro.dormir()
mi_perro.jugar()
mi_perro.ladrar()

# Crear una instancia de la clase Gato
mi_gato = Gato("Garfield", 3)

# Acceder a los atributos de la instancia
print(f"Nombre: {mi_gato.nombre}")
print(f"Edad: {mi_gato.edad}")

# Llamar a los métodos de la instancia
mi_gato.comer()
mi_gato.dormir()
mi_gato.jugar()
mi_gato.maullar()

# Path: Untitled-1.py