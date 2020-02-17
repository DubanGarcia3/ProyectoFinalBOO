import cx_Oracle

con = cx_Oracle.connect('pf','pf','XE')
cur = con.cursor()
class Empleado(object):
    def __init__(self, nombre, salario, num_hijos):
        self.nombre = nombre
        self.salario = salario
        self.num_hijos = num_hijos

empleado = Empleado("Viviana", 3000,0)


# Get Python representation of the Oracle user defined type UDT_BUILDING
objType = con.gettype("EMPLEADO")

# convert a Python Building object to the Oracle user defined type UDT_BUILDING
def EmpleadoInConverter(value):
    obj = objType.newobject()
    obj.NOMBRE  = value.nombre
    obj.SALARIO = value.salario
    obj.NUM_HIJOS   = value.num_hijos
    return obj

def InputTypeHandler(cursor, value, numElements):
    if isinstance(value, Empleado):
        return cursor.var(cx_Oracle.OBJECT, arraysize = numElements,
                inconverter = EmpleadoInConverter, typename = objType.name)


# With the input type handler, the bound Python object is converted
# to the required Oracle object before being inserted
cur.inputtypehandler = InputTypeHandler
cur.execute("insert into empleados_obj values (:1, :2)", (1, empleado))

con.commit()
cur.close()
con.close()