from lib2to3.fixer_util import attr_chain

import cx_Oracle

con = cx_Oracle.connect('pf','pf','XE')
cur = con.cursor()

class Contrato(object):

    def __init__(self, id, id_empleado, fecha_inicio, fecha_fin, salario, por_com):
        self.id = id
        self.id_empleado = id_empleado
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.salario = salario
        self.por_com = por_com

def dumpContrato(contrato, con ,prefix = ""):
    for attr in empleado.type.attributes:
        value = getattr(contrato, attr.name)
        if attr.name == 'ID' :
            con.id = repr(value)
        if attr.name == 'ID_EMPLEADO' :
            con.id_empleado = repr(value)
        if attr.name == 'FECHA_INICIO' :
            con.fecha_inicio = repr(value)
        if attr.name == 'FECHA_FIN' :
            con.fecha_fin = repr(value)
        if attr.name == 'SALARIO':
            con.salario = repr(value)
        if attr.name == 'POR_COM' :
            con.por_com = repr(value)
        print(prefix + "   " + attr.name + ":", repr(value))


cur.execute('select l.contrato from lista_contratos l')
for obj, in cur:
    contrato = Contrato()
    dumpContrato(obj, contrato)
    print contrato.id+" "+contrato.salario

cur.close()
con.close()
