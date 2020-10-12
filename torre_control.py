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


class TorreDeControl(Cola):
    
    def __init__(self):
        self.aterrizajes = Cola()
        self.despegues = Cola()

    def esta_vacia(self):
        return (self.aterrizajes.esta_vacia() and self.despegues.esta_vacia())

    def nuevo_arribo(self, avion):
        self.aterrizajes.encolar(avion)

    def nueva_partida(self, avion):
        self.despegues.encolar(avion)

    def asignar_pista(self):
        if self.esta_vacia():
            print('No hay vuelos en espera.')
            return
        if (not self.aterrizajes.esta_vacia()):
            print(f'El vuelo {self.aterrizajes.items[0]} aterrizo con exito')
            self.aterrizajes.desencolar()
        else:
            print(f'El vuelo {self.despegues.items[0]} despego con exito.')
            self.despegues.desencolar()

    def ver_estado(self):
        print(f'Vuelos esperando para aterrizar: {", ".join(self.aterrizajes.items)}'
              f'\nVuelos esperando para despegar:  {", ".join(self.despegues.items)}')

    def __repr__(self):
        return 'TorreDeControl()'


# Testeo
# torre = TorreDeControl()
# torre.nuevo_arribo('AR156')
# torre.nueva_partida('KLM1267')
# torre.nuevo_arribo('AR32')
# torre.ver_estado()
# print('Esta vacia?', torre.esta_vacia())
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# torre.asignar_pista()
# print('Esta vacia?', torre.esta_vacia())
