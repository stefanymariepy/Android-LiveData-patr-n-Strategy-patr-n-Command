# ==================================================
# SIMULACIÓN DE ANDROID LIVEDATA - PATRÓN OBSERVER
# ==================================================

class LiveData:
    def __init__(self):
        self.__valor = None           # Dato que queremos observar (privado)
        self.__observadores = []      # Lista de objetos que están escuchando

    # 📌 Registrar: Agrega alguien que quiere ser avisado
    def observar(self, funcion):
        self.__observadores.append(funcion)

    # 📌 Modificar valor: Cuando cambia, avisa a todos
    def set_valor(self, nuevo_valor):
        self.__valor = nuevo_valor
        # Recorre la lista y avisa a cada observador
        for obs in self.__observadores:
            obs(self.__valor)


# ----------------------
# USO DEL PROGRAMA
# ----------------------

# Función que simula la pantalla del celular
def actualizar_pantalla(dato):
    print(f"📱 Pantalla actualizada: {dato}")

# Función que simula una notificación
def mostrar_alerta(dato):
    print(f"🔔 Nueva alerta: {dato}")


# 1. Creamos el dato observable
datos_sensor = LiveData()

# 2. Decimos quiénes quieren enterarse de cambios
datos_sensor.observar(actualizar_pantalla)
datos_sensor.observar(mostrar_alerta)

# 3. Cambiamos el valor (AUTOMÁTICAMENTE avisa a todos)
print("--- Cambio 1 ---")
datos_sensor.set_valor("Temperatura: 24°C")

print("--- Cambio 2 ---")
datos_sensor.set_valor("Batería baja: 15%")