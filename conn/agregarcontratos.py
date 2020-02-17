import cx_Oracle
import time
con = cx_Oracle.connect('pf','pf','XE')
cur = con.cursor()
class Contrato(object):
    def __init__(self, id, id_empleado, fecha_inicio, fecha_fin, salario, por_com):
        self.id = id
        self.id_empleado = id_empleado
        self.fecha_inicio =fecha_inicio
        self.fecha_fin = fecha_fin
        self.salario = salario
        self.por_com = por_com

rpt_time = time.strftime('%Y-%m-%d %H:%M:%S')
rpt_time
contrato = Contrato(400, 101, rpt_time, rpt_time, 11111, 2);


# Get Python representation of the Oracle user defined type UDT_BUILDING
objType = con.gettype("CONTRATOSOBJ")

# convert a Python Building object to the Oracle user defined type UDT_BUILDING
def ContratoInConverter(value):
    obj = objType.newobject()
    obj.id = value.id
    obj.id_empleado = value.id_empleado
    obj.fecha_inicio = value.fecha_inicio
    obj.fecha_fin = value.fecha_fin
    obj.salario = value.salario
    obj.por_com = value.por_com
    return obj

def InputTypeHandler(cursor, value, numElements):
    if isinstance(value, Contrato):
        return cursor.var(cx_Oracle.OBJECT, arraysize = numElements,
                inconverter = ContratoInConverter, typename = objType.name)


# With the input type handler, the bound Python object is converted
# to the required Oracle object before being inserted
cur.inputtypehandler = InputTypeHandler
arr = [(2,contrato)]
add = ("insert into lista_contratos"
               "VALUES (?,?)")
cur.execute("insert into lista_contratos values (:1,:2)", (2,contrato))

con.commit()
cur.close()
con.close()