import cx_Oracle
con = cx_Oracle.connect('pf/pf')
cur = con.cursor()
returnVal = cur.callfunc("sumar", int, [25, 15])
print(returnVal)
cur.close()
con.close()