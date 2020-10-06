# -*- coding: utf8 -*-

# torre_control.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 8.12: Torre de Control (Colas)


class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl():
    
    def __init__(self):
        self.cola_aterrizaje = []
        self.cola_despegue = []

    def esta_vacia(self):
        return (len(self.cola_aterrizaje) == 0 and len(self.cola_despegue) == 0)

    def nuevo_arribo(self, avion):
        self.cola_aterrizaje.append(avion)

    def nueva_partida(self, avion):
        self.cola_despegue.append(avion)

    def asignar_pista(self):
        if self.esta_vacia():
            print('No hay vuelos en espera.')
            return
        if (self.cola_aterrizaje):
            print(f'El vuelo {self.cola_aterrizaje[0]} aterrizo con exito')
            return self.cola_aterrizaje.pop(0)
        print(f'El vuelo {self.cola_despegue[0]} despego con exito.')
        return self.cola_despegue.pop(0)

    def ver_estado(self):
        print(f'Vuelos esperando para aterrizar: {", ".join(self.cola_aterrizaje)}'
              f'\nVuelos esperando para despegar:  {", ".join(self.cola_despegue)}')

    def __repr__(self):
        return f'TorreDeControl()'


# Testeo
# torre = TorreDeControl()
# torre.nuevo_arribo('AR156')
# torre.nueva_partida('KLM1267')
# torre.nuevo_arribo('AR32')
# torre.ver_estado()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
