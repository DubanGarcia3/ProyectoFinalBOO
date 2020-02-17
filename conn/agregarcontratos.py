import cx_Oracle
import time
import datetime
con = cx_Oracle.connect('pf','pf','XE')
cur = con.cursor()
class Contrato(object):
    def __init__(self, ID, ID_EMPLEADO, FECHA_INICIO, FECHA_FIN, SALARIO, POR_COM):
        self.ID = ID
        self.ID_EMPLEADO = ID_EMPLEADO
        self.FECHA_INICIO = FECHA_INICIO
        self.FECHA_FIN = FECHA_FIN
        self.SALARIO = SALARIO
        self.POR_COM = POR_COM

rpt_time = time.strftime('%Y-%m-%d %H:%M:%S')
rpt_time
d = datetime.datetime.now()
contrato = Contrato(400, 101, d, d, 11111, 2)


# Get Python representation of the Oracle user defined type UDT_BUILDING
objType = con.gettype("CONTRATOSOBJ")

# convert a Python Building object to the Oracle user defined type UDT_BUILDING
def ContratoInConverter(value):
    obj = objType.newobject()
    obj.ID = value.ID
    obj.ID_EMPLEADO = value.ID_EMPLEADO
    obj.FECHA_INICIO = value.FECHA_INICIO
    obj.FECHA_FIN = value.FECHA_FIN
    obj.SALARIO = value.SALARIO
    obj.POR_COM = value.POR_COM
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
arr = (2, contrato)
add = ("insert into lista_contratos"
               "VALUES (?,?)")
cur.execute("insert into lista_contratos (id, contrato) values (:1,:2)", arr)
cur.execute("insert into lista_contratos values (:1,:2)", (2,contrato))
con.commit()
cur.close()
con.close()