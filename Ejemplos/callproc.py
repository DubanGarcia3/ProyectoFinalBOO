import cx_Oracle
con = cx_Oracle.connect('ProyectoFinal/123@localhost')
cur = con.cursor()
#cur = con.cursor()
outVar = cur.var(cx_Oracle.STRING)
#inVar = cur.var(cx_Oracle.STRING)
#inVar = "8006330575"
cur.callproc('format_phone', ["8006330575", outVar])
#print(outVar.getvalue())
print(outVar)
cur.close()
con.close()