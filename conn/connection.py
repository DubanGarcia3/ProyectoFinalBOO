import cx_Oracle
con = cx_Oracle.connect('pf','pf','XE')
cur = con.cursor()
cur.execute('select count(id) from lista_contratos')
for result in cur:
	print result
cur.close()
con.close()