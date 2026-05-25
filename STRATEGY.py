# ==================================================
# SELECCIÓN DE OPTIMIZADORES EN IA - PATRÓN STRATEGY
# ==================================================

# ----------------------
# ESTRATEGIAS (ALGORITMOS)
# Cada uno es una forma distinta de hacer la tarea
# ----------------------
class OptimizadorSGD:
    def optimizar(self):
        # 📌 Algoritmo 1: Descenso de Gradiente Estocástico
        return "⚙️ Usando SGD: Bueno para conjuntos de datos grandes"

class OptimizadorAdam:
    def optimizar(self):
        # 📌 Algoritmo 2: Adam (el más usado)
        return "⚙️ Usando Adam: Rápido y eficiente, el más popular"

class OptimizadorRMSprop:
    def optimizar(self):
        # 📌 Algoritmo 3: RMSprop
        return "⚙️ Usando RMSprop: Ideal para redes neuronales recurrentes"


# ----------------------
# CONTEXTO
# Es el sistema que usa la estrategia, no le importa cuál sea
# ----------------------
class ModeloIA:
    def __init__(self, estrategia):
        # Recibe CUALQUIER estrategia que tenga el método 'optimizar'
        self.estrategia = estrategia

    # 📌 Permite cambiar de estrategia en cualquier momento
    def cambiar_estrategia(self, nueva_estrategia):
        self.estrategia = nueva_estrategia

    def entrenar(self):
        # Ejecuta la estrategia actual
        print(f"Iniciando entrenamiento... {self.estrategia.optimizar()}")


# ----------------------
# USO DEL PROGRAMA
# ----------------------

# 1. Creamos el modelo y elegimos la primera estrategia
red_neuronal = ModeloIA(OptimizadorAdam())
red_neuronal.entrenar()

# 2. Probamos con otra estrategia DIFERENTE sin modificar el modelo
red_neuronal.cambiar_estrategia(OptimizadorSGD())
red_neuronal.entrenar()

# 3. Probamos otra más
red_neuronal.cambiar_estrategia(OptimizadorRMSprop())
red_neuronal.entrenar()