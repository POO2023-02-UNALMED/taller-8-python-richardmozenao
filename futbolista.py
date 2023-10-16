from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, p):
        self._golesMarcados = p

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self, p):
        self._tarjetasRojas = p

    def getListaFutbolistas(cls):
        return cls.listaFutbolistas
    
    def setListaFutbolistas(cls, p):
        cls.listaFutbolistas = p

    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self, p):
        self._piernaHabil = p

    def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre(), self.getDeporte(), self.getEdad(), self.getAñosPracticando())

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, p):
        self._golesMarcados = p

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self, p):
        self._tarjetasRojas = p

