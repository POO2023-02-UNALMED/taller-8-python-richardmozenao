class Deportista:
    def __init__(self, deporte, añosPracticando) -> None:
        self.deporte = deporte
        self.añosPracticando = añosPracticando
        
    def getDeporte(self):
        return self.deporte
    
    def setDeporte(self, p):
        self.deporte = p

    def getAñosPracticando(self):
        return self.añosPracticando
    
    def setAñosPracticando(self, p):
        self.añosPracticando = p
