#include <iostream>
#include <vector>
using namespace std;

// ==================================================
// CONTROL DE ACCIONES EN VIDEOJUEGOS - PATRÓN COMMAND
// ==================================================

// ----------------------
// INTERFAZ COMÚN
// Todas las acciones deben tener estos 2 métodos
// ----------------------
class Comando {
public:
    virtual void ejecutar() = 0; // Hacer la acción
    virtual void deshacer() = 0; // Revertir la acción
    virtual ~Comando() {}
};

// ----------------------
// RECEPTOR: EL JUGADOR
// Es quien realmente sabe moverse, saltar, etc.
// ----------------------
class Jugador {
public:
    void saltar()     { cout << "👤 Jugador: SALTA hacia arriba" << endl; }
    void agacharse()  { cout << "👤 Jugador: Se AGRACHA en el suelo" << endl; }
    void moverIzq()   { cout << "👤 Jugador: Se mueve a la IZQUIERDA" << endl; }
    void moverDer()   { cout << "👤 Jugador: Se mueve a la DERECHA" << endl; }
};

// ----------------------
// COMANDOS CONCRETOS
// Envuelven la acción para que sea un objeto
// ----------------------
class ComandoSaltar : public Comando {
    Jugador* jugador;
public:
    ComandoSaltar(Jugador* j) : jugador(j) {}
    void ejecutar() override { jugador->saltar(); }   // 📌 Llama a la acción real
    void deshacer() override { jugador->agacharse(); }// 📌 Deshacer: bajar
};

class ComandoMoverIzq : public Comando {
    Jugador* jugador;
public:
    ComandoMoverIzq(Jugador* j) : jugador(j) {}
    void ejecutar() override { jugador->moverIzq(); }
    void deshacer() override { jugador->moverDer(); } // 📌 Deshacer: ir al lado contrario
};

// ----------------------
// INVOCADOR: EL CONTROL
// Recibe las teclas y ejecuta los comandos
// ----------------------
class ControlJuego {
    vector<Comando*> historial; // 📌 Guarda lo que hicimos para deshacer

public:
    void presionarBoton(Comando* accion) {
        accion->ejecutar();         // Ejecuta la acción
        historial.push_back(accion); // La guarda en el historial
    }

    void deshacerUltimaAccion() {
        if (!historial.empty()) {
            cout << "↩️  DESHACIENDO ÚLTIMA ACCIÓN..." << endl;
            historial.back()->deshacer(); // Llama al método deshacer
            historial.pop_back();         // Borra del registro
        }
    }
};

// ----------------------
// USO DEL PROGRAMA
// ----------------------
int main() {
    // Creamos al personaje
    Jugador* mario = new Jugador();

    // Creamos los comandos vinculados al personaje
    ComandoSaltar* cmdSaltar = new ComandoSaltar(mario);
    ComandoMoverIzq* cmdIzquierda = new ComandoMoverIzq(mario);

    // El control del juego
    ControlJuego* control = new ControlJuego();

    cout << "--- CONTROLES DEL JUEGO ---" << endl;
    control->presionarBoton(cmdIzquierda); // Tecla Flecha Izq
    control->presionarBoton(cmdSaltar);   // Tecla Espacio

    cout << "\n--- ERROR, QUIERO VOLVER ATRÁS ---" << endl;
    control->deshacerUltimaAccion(); // Vuelve a caer del salto
    control->deshacerUltimaAccion(); // Vuelve a moverse a la derecha

    // Liberar memoria
    delete cmdSaltar; delete cmdIzquierda; delete mario; delete control;
    return 0;
}