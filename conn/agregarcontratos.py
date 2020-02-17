import cx_Oracle

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

contrato = Contrato(400, 101, TO_DATE('07/01/2018','dd/MM/yyyy'), TO_DATE('07/01/2018','dd/MM/yyyy'), 828116, 2);


# Get Python representation of the Oracle user defined type UDT_BUILDING
objType = con.gettype("CONTRATOSOBJ")

# convert a Python Building object to the Oracle user defined type UDT_BUILDING
def EmpleadoInConverter(value):
    obj = objType.newobject()
    obj.id = id
    obj.id_empleado = id_empleado
    obj.fecha_inicio = fecha_inicio
    obj.fecha_fin = fecha_fin
    obj.salario = salario
    obj.por_com = por_com
    return obj

def InputTypeHandler(cursor, value, numElements):
    if isinstance(value, Empleado):
        return cursor.var(cx_Oracle.OBJECT, arraysize = numElements,
                inconverter = EmpleadoInConverter, typename = objType.name)


# With the input type handler, the bound Python object is converted
# to the required Oracle object before being inserted
cur.inputtypehandler = InputTypeHandler
cur.execute("insert into empleados_obj values (:1, :2)", (1, contrato))

con.commit()
cur.close()
con.close()