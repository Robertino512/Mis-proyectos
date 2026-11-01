from Empleado import Empleado
class EmpleadoContratado(Empleado):
    remuneracion_mensual=0
    def __init__(self,legajo:int,nombre:str,apellido:str,cant_horas_mes:int, valor_hora:float,supervisor:None):
        super().__init__(legajo,nombre,apellido,supervisor)
        self.cant_horas_mes:int=cant_horas_mes
        self.valor_hora:float= valor_hora
        
        

    def calcular_remuneracion(self):
        self.remuneracion_mensual= self.cant_horas_mes*self.valor_hora
        return self.remuneracion_mensual

    def check_valor_hora(self):
        if self.valor_hora<0:
            return False
        else:
            return True


    def tiene_supervisor(self):
        if self.supervisor==None:
            return ('Sin supervisor')
        else:
            return (self.supervisor.nombre)

    def mostrar(self):
        return f'Legajo: {self.legajo} - Nombre: {self.nombre} - Apellido: {self.apellido} - Cantidad de horas por mes: {self.cant_horas_mes} - Valor x hora: {self.valor_hora} Supervisor: {self.tiene_supervisor()} - Remuneracion mensual: {self.calcular_remuneracion()}'

    


    

        