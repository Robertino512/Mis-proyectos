from EmpleadoContratado import EmpleadoContratado
from EmpleadoPermanente import EmpleadoPermanente
from Departamento import Departamento

def main():
    empleadoContratado1=EmpleadoContratado(legajo=3829,nombre='Julio',apellido='Gomez',cant_horas_mes=90, valor_hora=30.5 ,supervisor=None)
    empleadoContratado2=EmpleadoContratado(legajo=9493,nombre='Hernan',apellido='Serrano',cant_horas_mes=67, valor_hora=45.3 ,supervisor=empleadoContratado1)
    empleadoPermanente1=EmpleadoPermanente(legajo=5920,nombre='Joaco',apellido='Fernandez',sueldo_basico=600.45, antiguedad=4, supervisor=None)
    empleadoPermanente2=EmpleadoPermanente(legajo=4593,nombre='Rodrigo',apellido='munioz',sueldo_basico=135, antiguedad=10, supervisor=empleadoContratado2)
    empleados=[empleadoContratado1,empleadoContratado2,empleadoPermanente1,empleadoPermanente2]
    for i in empleados:
        print(i.mostrar())

    departamento1=Departamento(codigo=1, nombre='Bienes', empleados=empleados)
    departamento2=Departamento(codigo=2,nombre='Salud', empleados=empleados)
    empleadoagregar=EmpleadoContratado(legajo=9499,nombre='Roman',apellido='Riquelme',cant_horas_mes=20, valor_hora=90.5 ,supervisor=None)

    departamento1.agregar_empleado(empleadoagregar)
    departamento1.consultar_empleado(empleadoagregar)
    departamento1.quitar_empleado(empleadoagregar)
    departamento2.agregar_empleado(empleadoagregar)
    departamento2.consultar_empleado(empleadoagregar)
    


if '__name__'==main():
    main()
