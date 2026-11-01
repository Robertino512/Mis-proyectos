from Empleado import Empleado
class EmpleadoPermanente(Empleado):
    remuneracion_mensual=0
    def __init__(self,legajo:int,nombre:str,apellido:str,sueldo_basico:float, antiguedad:int, supervisor:None):
        super().__init__(legajo,nombre,apellido,supervisor)
        self.sueldo_basico:float =sueldo_basico
        self.antiguedad:int=antiguedad
    
    def calcular_remuneracion(self):
        adicional=self.antiguedad*0.02
        self.remuneracion_mensual=self.sueldo_basico+self.sueldo_basico*adicional
        return self.remuneracion_mensual

    def check_sueldo(self):
        if self.valor_hora<0:
            return False
        else:
            return True

    def mostrar(self):
     return f'Legajo: {self.legajo} - Nombre: {self.nombre} - Apellido: {self.apellido} - Sueldo basico: {self.sueldo_basico} - Supervisor: {self.tiene_supervisor()} - Anios de antiguedad: {self.antiguedad} - Remuneracion mensual: {self.calcular_remuneracion():.2f}'


    def tiene_supervisor(self):
            if self.supervisor==None:
                    return ('Sin supervisor')
            else:
                    return self.supervisor.nombre