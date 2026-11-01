from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, legajo:int,nombre:str,apellido:str, supervisor:None):
        self.legajo:int= legajo
        self.nombre:str=nombre
        self.apellido:str=apellido
        self.supervisor:None= supervisor

    @abstractmethod
    def mostrar(self):
        return f'Legajo: {self.legajo} - Nombre: {self.nombre} - Apellido: {self.apellido} '

    @abstractmethod
    def tiene_supervisor(self):
        if self.supervisor==None:
                return ('Sin supervisor') 
        else:
                return self.supervisor.nombre


