#from typing import Self


#class celulares:
    #def__init__(Self, marca, modelo, precio):
        #Self.marca = marca
        #Self.modelo = modelo
        #Self.precio = precio
    
    #def__str__(Self):
        #return f"Marca: {Self.marca}, modelo: {Self.modelo}, precio: {Self.precio}"

#class celulares_con_camara(celulares):
    #def__init__(Self, marca, modelo, precio, resolucion):
        #super().__init__(marca, modelo, precio)
        #Self.resolucion = resolucion
    
    #def__str__(Self):
        #return f"{super().__str__()}, resolucion: {Self.resolucion}"

#class celulares_con_camara_y_red(celulares_con_camara):
    #def__init__(Self, marca, modelo, precio, resolucion, red):
        #super().__init__(marca, modelo, precio, resolucion)
        #Self.red = red
    
    #def__str__(Self):
        #return f"{super().__str__()}, red: {Self.red}"

#class celulares_con_camara_y_red_y_wifi(celulares_con_camara_y_red):
    #def__init__(Self, marca, modelo, precio, resolucion, red, wifi):
        #super().__init__(marca, modelo, precio, resolucion, red)
        #Self.wifi = wifi
    
    #def__str__(Self):
        #return f"{super().__str__()}, wifi: {Self.wifi}"


#celular1 = celulares("Samsung", "Galaxy S21", 1000)
#celular2 = celulares_con_camara("Samsung", "Galaxy S21", 1000, "12MP")
#celular3 = celulares_con_camara_y_red("Samsung", "Galaxy S21", 1000, "12MP", "4G")
#celular4 = celulares_con_camara_y_red_y_wifi("Samsung", "Galaxy S21", 1000, "12MP", "4G", "802.11n")

#print(celular1)
#print(celular2)
#print(celular3)
#print(celular4)

#Marca: Samsung, modelo: Galaxy S21, precio: 1000
#Marca: Samsung, modelo: Galaxy S21, precio: 1000, resolucion: 12MP
#Marca: Samsung, modelo: Galaxy S21, precio: 1000, resolucion: 12MP, red: 4G
#Marca: Samsung, modelo: Galaxy S21, precio: 1000, resolucion: 12MP, red: 4G, wifi: 802.11n

#En este caso, se crearon 4 clases, la primera es la clase celulares, la segunda es la clase celulares_con_camara, la tercera es la clase celulares_con_camara_y_red y la cuarta es la clase celulares_con_camara_y_red_y_wifi.

#La clase celulares_con_camara hereda de la clase celulares, la clase celulares_con_camara_y_red hereda de la clase celulares_con_camara y la clase celulares_con_camara_y_red_y_wifi hereda de la clase celulares_con_camara_y_red.

#En cada clase se sobreescribe el metodo __str__ para que muestre los atributos de la clase y de las clases de las que hereda.

#Se crean 4 objetos, uno de cada clase, y se imprime cada uno de ellos. Se puede ver que cada objeto tiene los atributos de la clase y de las clases de las que hereda.

#En el caso de la clase celulares_con_camara_y_red_y_wifi, se puede ver que tiene los atributos de la clase celulares, de la clase celulares_con_camara, de la clase celulares_con_camara_y_red y de la clase celulares_con_camara_y_red_y_wifi.

#En este caso, se puede ver que se puede heredar de varias clases, no solo de una.

#como seria con herencia multiple en python

#class celulares:
    #def__init__(Self, marca, modelo, precio):
        #Self.marca = marca
        #Self.modelo = modelo
        #Self.precio = precio
    
    #def__str__(Self):
        #return f"Marca: {Self.marca}, modelo: {Self.modelo}, precio: {Self.precio}"

#class camara:
    #def__init__(Self, resolucion):
        #Self.resolucion = resolucion
    
    #def__str__(Self):
        #return f"resolucion: {Self.resolucion}"

#class red:

    #def__init__(Self, red):
        #Self.red = red
    
    #def__str__(Self):
        #return f"red: {Self.red}"

#class wifi:

    #def__init__(Self, wifi):
        #Self.wifi = wifi
    
    #def__str__(Self):
        #return f"wifi: {Self.wifi}"

#class celulares_con_camara(celulares, camara):
    #def__init__(Self, marca, modelo, precio, resolucion):
        #celulares.__init__(Self, marca, modelo, precio)
        #camara.__init__(Self, resolucion)
    
    #def__str__(Self):
        #return f"{celulares.__str__(Self)}, {camara.__str__(Self)}"

#class celulares_con_camara_y_red(celulares, camara, red):
    #def__init__(Self, marca, modelo, precio, resolucion, red):
        #celulares.__init__(Self, marca, modelo, precio)
        #camara.__init__(Self, resolucion)
        #red.__init__(Self, red)
    
    #def__str__(Self):
        #return f"{celulares.__str__(Self)}, {camara.__str__(Self)}, {red.__str__(Self)}"

#class celulares_con_camara_y_red_y_wifi(celulares, camara, red, wifi):
    #def__init__(Self, marca, modelo, precio, resolucion, red, wifi):
        #celulares.__init__(Self, marca, modelo, precio)
        #camara.__init__(Self, resolucion)
        #red.__init__(Self, red)
        #wifi.__init__(Self, wifi)
    
    #def__str__(Self):
        #return f"{celulares.__str__(Self)}, {camara.__str__(Self)}, {red.__str__(Self)}, {wifi.__str__(Self)}"

#celular1 = celulares("Samsung", "Galaxy S21", 1000)
#celular2 = celulares_con_camara("Samsung", "Galaxy S21", 1000, "12MP")
#celular3 = celulares_con_camara_y_red("Samsung", "Galaxy S21", 1000, "12MP", "4G")
#celular4 = celulares_con_camara_y_red_y_wifi("Samsung", "Galaxy S21", 1000, "12MP", "4G", "802.11n")

#print(celular1)
#print(celular2)
#print(celular3)
#print(celular4)

#Marca: Samsung, modelo: Galaxy S21, precio: 1000
#Marca: Samsung, modelo: Galaxy S21, precio: 1000, resolucion: 12MP
#Marca: Samsung, modelo: Galaxy S21, precio: 1000, resolucion: 12MP, red: 4G
#Marca: Samsung, modelo: Galaxy S21, precio: 1000, resolucion: 12MP, red: 4G, wifi: 802.11n

#En este caso, se crearon 4 clases, la primera es la clase celulares, la segunda es la clase camara, la tercera es la clase red y la cuarta es la clase wifi.

#Las clases camara, red y wifi no heredan de ninguna clase, solo tienen un atributo y un metodo __str__ que muestra el atributo.

#Las clases celulares_con_camara, celulares_con_camara_y_red y celulares_con_camara_y_red_y_wifi heredan de la clase celulares y de las clases camara, red y wifi.

#En cada clase se sobreescribe el metodo __str__ para que muestre los atributos de la clase y de las clases de las que hereda.

#Se crean 4 objetos, uno de cada clase, y se imprime cada uno de ellos. Se puede ver que cada objeto tiene los atributos de la clase y de las clases de las que hereda.

#En el caso de la clase celulares_con_camara_y_red_y_wifi, se puede ver que tiene los atributos de la clase celulares, de la clase camara, de la clase red y de la clase wifi.

#En este caso, se puede ver que se puede heredar de varias clases, no solo de una.

class motos:
    def __init__(self, marca, modelo, cilindraje, potencia):
        self.marca = marca
        self.modelo = modelo
        self.cilindraje = cilindraje
        self.potencia = potencia
    
    def __str__(self):
        return f"Marca: {self.marca}, modelo: {self.modelo}, cilindraje: {self.cilindraje}, potencia: {self.potencia}"
    
class motos_con_frenos(motos):
    def __init__(self, marca, modelo, cilindraje, potencia, frenos):
        super().__init__(marca, modelo, cilindraje, potencia)
        self.frenos = frenos
    
    def __str__(self):
        return f"{super().__str__()}, frenos: {self.frenos}"

class motos_con_frenos_y_llantas(motos_con_frenos):
    def __init__(self, marca, modelo, cilindraje, potencia, frenos, llantas):
        super().__init__(marca, modelo, cilindraje, potencia, frenos)
        self.llantas = llantas
    
    def __str__(self):
        return f"{super().__str__()}, llantas: {self.llantas}"

class motos_con_frenos_y_llantas_y_asientos(motos_con_frenos_y_llantas):
    def __init__(self, marca,modelo, cilindraje, potencia, frenos, llantas, asientos):
        super().__init__(marca, modelo, cilindraje, potencia, frenos, llantas)
        self.asientos = asientos
    
    def __str__(self):
        return f"{super().__str__()}, asientos: {self.asientos}"

moto1 = motos("Bajaj", "ns", 200, 26)
moto2 = motos_con_frenos("Bajaj", "ns", 200, "26hp", "ABS")
moto3 = motos_con_frenos_y_llantas("Bajaj", "ns", 200, "26hp", "ABS", "Pirelli")
moto4 = motos_con_frenos_y_llantas_y_asientos("Bajaj", "ns", 200, "26hp", "ABS", "Pirelli", "cuero")

print(moto1)
print(moto2)
print(moto3)
print(moto4)

#Marca: Bajaj, modelo: ns, cilindraje: 200, potencia: 26hp
#Marca: Bajaj, modelo: ns, cilindraje: 200, potencia: 26hp, frenos: ABS


