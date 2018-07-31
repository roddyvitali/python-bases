# Modelado de un auto

# TODO: Se le podria agregar que al retornar el tiempo, lo divida en "HH:MM:SS".
# TODO: Se podria agregar que vaya acelerando a medida que se va moviendo.
class Auto:
    _Autos = ['''
                    _______
                  _/\______\\__
                 / ,-. -|-  ,-.`-.
                 `( o )----( o )-'
                   `-'      `-''',
                    '''
                    _______
            _-_-  _/\______\\__
         _-_-__  / ,-. -|-  ,-.`-.
            _-_- `( o )----( o )-'
                   `-'      `-'''
            ]

    def __init__(self):
        self._is_turned_on = False
        self.set_deffaul_values()

    def __init__(self, _is_turned_on):
        self._is_turned_on = _is_turned_on
        self.set_deffaul_values()

    def set_deffaul_values(self):
        self._current_speed = 0
        self._capacidad_maxima_nafta = 20000
        self._nafta_level = self._capacidad_maxima_nafta
        self._velocidad_maxima = 200
        self._consumo_nafta_por_metro = 2
        self._capacidad_maxima_personas = 5
        self._personas_a_bordo = 1
        self._metros_recorridos = 0
        self._tiempo_en_viaje = 0

    def encender(self):
        self._is_turned_on = True
        self.mostrar_estado()

    def apagar(self):
        if (self._is_turned_on and self._current_speed == 0):
            self._is_turned_on = False
            self.mostrar_estado()
        else:
            print("\t ERROR - El auto debe estar quieto.")

    # Se utiliza para definir la velocidad del auto al moverse (debería ir acelerando a medida que se mueve, pero bueno Já)
    def acelerar(self, velocidad_a_incrementar):
        if (self._is_turned_on):
            if (velocidad_a_incrementar > 0):
                if ((self._velocidad_maxima - self._current_speed) - velocidad_a_incrementar >= 0):
                    self._current_speed += velocidad_a_incrementar
                else:
                    self._current_speed = self._velocidad_maxima
        else:
            print("\t ERROR - Debe encender el auto primero.")

    def frenar(self, velocidad_a_reducir):
        if (self._is_turned_on):
            if (velocidad_a_reducir > 0):
                if (self._current_speed - velocidad_a_reducir >= 0):
                    self._current_speed -= velocidad_a_reducir
        else:
            print("\t ERROR - Debe encender el auto primero.")

    def cargar_nafta(self, _cantidad_litros):
        if (_cantidad_litros > 0):
            if (self._nafta_level + _cantidad_litros <= self._capacidad_maxima_nafta):
                self._nafta_level += _cantidad_litros
            else:
                self._nafta_level = self._capacidad_maxima_nafta
        else:
            print("\t ERROR - No se puede cargar esa cantidad.")

    # Recibe los metros que se quiere mover el auto, y calcula cuanta nafata consume. Retorna los metros que logra recorrer.
    def metros_posibles_restar_nafta(self, _metros_recorrer):
        if (self._is_turned_on and self._current_speed > 0):
            consumo_personas = (1 + float(self._personas_a_bordo / 10))
            costo_por_metro = self._consumo_nafta_por_metro * consumo_personas
            nafta_por_consumir = (costo_por_metro * _metros_recorrer)

            if self._nafta_level - nafta_por_consumir > 0:
                self._nafta_level -= nafta_por_consumir
                return _metros_recorrer # Recorrio todo esto
            else:
                metros_recorridos = int(self._nafta_level / (consumo_personas * self._consumo_nafta_por_metro))
                self._nafta_level = 0
                return metros_recorridos
        else:
            print("\t ERROR - El auto debe estar en movimiento.")
            return0

    # Para moverse, utiliza la velocidad que fue puesta al "acelerar()"
    def moverse(self, _cantidad_metros_recorrer):
        if (self._is_turned_on):
            metrosRecorridos = self.metros_posibles_restar_nafta(_cantidad_metros_recorrer)
            self._metros_recorridos += metrosRecorridos
            self._tiempo_en_viaje += int(metrosRecorridos / self._current_speed * 1000)

            if (self._nafta_level == 0):
                self._is_turned_on = False
                self._current_speed = 0
        else:
            print("\t ERROR - Debe encender el auto primero.")

    def subir_personas(self, _cantidad_personas):
        if (_cantidad_personas > 0):
            if (self._personas_a_bordo + _cantidad_personas < self._capacidad_maxima_personas):
                self._personas_a_bordo += _cantidad_personas
            else:
                self._personas_a_bordo = self._capacidad_maxima_personas

    def bajar_personas(self, _cantidad_personas):
        if (_cantidad_personas > 0):
            if (self._personas_a_bordo - _cantidad_personas >= 0):
                self._personas_a_bordo -= _cantidad_personas
        else:
            print("\t ERROR - No puede haber una cantidad negativa de personas")

    def mostrar_estado(self):
        if self._is_turned_on:
            print(self._Autos[1])
        else:
            print(self._Autos[0])

    # Muestra todas las variables y constantes del Auto
    def mostrar_valores(self):
        print('''
                Estado: {0},
                Velocidad: {1} Km/h,
                Capacidad Máxima Nafta: {2},
                Nivel de Nafta: {3},
                Velocidad Máxima Posible: {4} Km/h,
                Consumo Por Metro: {5},
                Capacidad Máxima Personas: {6},
                Personas a Bordo: {7},
                Metros Recorridos: {8},
                Tiempo en viaje: {9} Hs
              '''.format(
                  self._is_turned_on,
                  self._current_speed,
                  self._capacidad_maxima_nafta,
                  self._nafta_level,
                  self._velocidad_maxima,
                  self._consumo_nafta_por_metro,
                  self._capacidad_maxima_personas,
                  self._personas_a_bordo,
                  self._metros_recorridos,
                  self._tiempo_en_viaje / 1000
              ))

def run():
    auto1 = Auto(_is_turned_on=True)

    while True:
        commando = str(input('''
                             ¿Qué desea hacer?

                             [E]ncender.
                             [A]pagar.
                             [Ac]elerar.
                             [F]renar.
                             [M]over.
                             [Su]bir personas.
                             [B]ajar personas.
                             [C]argar nafta.
                             [Mo]strar TODO.
                             [S]alir.
                             \n\t Eleccion: ''')).lower()
        if commando == "e":
            auto1.encender()
        elif commando == "a":
            auto1.apagar()
        elif commando == "ac":
            auto1.acelerar(int(input("Velocidad incrementar: ")))
        elif commando == "f":
            auto1.frenar(int(input("Velocidad reducir: ")))
        elif commando == "m":
            auto1.moverse(int(input("Cantidad kilometros a recorrer: ")))
        elif commando == "su":
            auto1.subir_personas(int(input("Cantidad personas suben: ")))
        elif commando == "b":
            auto1.bajar_personas(int(input("Cantidad personas bajan: ")))
        elif commando == "c":
            auto1.cargar_nafta(int(input("Cantidad litros cargar: ")))
        elif commando == "mo":
            auto1.mostrar_estado()
            auto1.mostrar_valores()
        elif commando == "s":
            break
        else:
            break

try:
    run()
except KeyboardInterrupt:
    print("\n\n\t Adios!!!")