from lib2to3.fixer_util import attr_chain

import cx_Oracle

con = cx_Oracle.connect('pf','pf','XE')
cur = con.cursor()

class Empleado(object):
    def __init__(self, nombre, salario, num_hijos):
        self.nombre = nombre
        self.salario = salario
        self.num_hijos = num_hijos

    def __init__(self):
        self.nombre = ''
        self.salario = 0
        self.num_hijos = 0

def dumpEmpleado(empleado, emp ,prefix = ""):
    for attr in empleado.type.attributes:
        value = getattr(empleado, attr.name)
        if attr.name == 'NOMBRE' :
            emp.nombre = repr(value)
        if attr.name == 'SALARIO' :
            emp.salario = repr(value)
        if attr.name == 'NUM_HIJOS' :
            emp.num_hijos = repr(value)
        print(prefix + "   " + attr.name + ":", repr(value))


cur.execute('select empleado from empleados_obj')
for obj, in cur:
    empleado = Empleado()
    dumpEmpleado(obj, empleado)
    print empleado.nombre+" "+empleado.salario

cur.close()
con.close()
