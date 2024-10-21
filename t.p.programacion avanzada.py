import random

class Tablero:
    def __init__(self, lado):
        self.lado = lado
        self.genes = self.generar_genes()

    def generar_genes(self):
        return [random.randint(1, self.lado) for _ in range(self.lado)]

    def mutar(self):
        indiceAleatorio = random.randint(0, self.lado - 1)
        nuevoValor = random.randint(1, self.lado)
        self.genes[indiceAleatorio] = nuevoValor

    def fitness(self):
        diagonal = 0
        horizontal = len(self.genes) - len(set(self.genes))
        numero = len(self.genes)
        for indiceI in range(numero):
            for indiceJ in range(indiceI + 1, numero):
                if abs(indiceI - indiceJ) == abs(self.genes[indiceI] - self.genes[indiceJ]):
                    diagonal += 1
        return horizontal + diagonal

    def __str__(self):
        n = len(self.genes)
        dibujo = []
        for i in range(n):
            dibujo.append(list("." * n))
            for k in range(n):
                if self.genes[k] - 1 == i:
                    dibujo[i][k] = "R"
            dibujo[i] = " ".join(dibujo[i])
        return "\n".join(dibujo) + "\nfitness: " + str(self.fitness())

class NReinas:
    def __init__(self, lado, max_iteraciones=5000, max_poblacion=50):
        self.lado = lado
        self.max_iteraciones = max_iteraciones
        self.max_poblacion = max_poblacion
        self.poblacion = self.generar_poblacion_inicial()

    def generar_poblacion_inicial(self):
        return [Tablero(self.lado) for _ in range(self.max_poblacion)]

    def rankear(self):
        return sorted(self.poblacion, key=lambda tablero: tablero.fitness())

    def cruzar_y_mutar(self, poblacion_ordenada):
        mitad = self.max_poblacion // 2
        medio = self.lado // 2
        nuevos_tableros = []

        for i in range(0, mitad, 2):
            if i + 1 < len(poblacion_ordenada):
                padre = poblacion_ordenada[i].genes
                madre = poblacion_ordenada[i + 1].genes
                hijo1_genes = padre[:medio] + madre[medio:]
                hijo2_genes = madre[:medio] + padre[medio:]

                hijo1 = Tablero(self.lado)
                hijo2 = Tablero(self.lado)
                hijo1.genes = hijo1_genes
                hijo2.genes = hijo2_genes

                if random.random() > 0.70:
                    hijo1.mutar()
                    hijo2.mutar()

                nuevos_tableros.append(hijo1)
                nuevos_tableros.append(hijo2)

        while len(nuevos_tableros) < self.max_poblacion:
            nuevos_tableros.append(Tablero(self.lado))

        return nuevos_tableros

    def resolver(self):
        for generacion in range(self.max_iteraciones):
            poblacion_rankeada = self.rankear()
            if poblacion_rankeada[0].fitness() == 0:
                print(poblacion_rankeada[0])
                print(f"Solución encontrada en {generacion + 1} generaciones")
                return
            self.poblacion = self.cruzar_y_mutar(poblacion_rankeada)
        
        print(f"No se encontró solución en {self.max_iteraciones} generaciones")

# Valores iniciales
LADO = 8
MAXIMO_ITERACIONES = 5000
MAXIMO_POBLACION = 50

# Ejecutar la solución
nreinas = NReinas(LADO, MAXIMO_ITERACIONES, MAXIMO_POBLACION)
nreinas.resolver()
