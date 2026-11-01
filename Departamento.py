class Departamento:
    def __init__(self, codigo:int,nombre:str,empleados:list):
        self.codigo:int=codigo
        self.nombre:str=nombre
        self.empleados:list=empleados

    def agregar_empleado(self, empleado):
        return self.empleados.append(empleado)

    def quitar_empleado(self,empleado):
        return self.empleados.remove(empleado)

    def consultar_empleado(self,empleado):
        if empleado in self.empleados:
            print (f'El empleado existe en nuestro departamento {self.nombre}')
        else: 
            print (f'El empleado no es correspondiente a nuestro departamento {self.nombre}')

