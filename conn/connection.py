import cx_Oracle
con = cx_Oracle.connect('pf','pf','XE')
cur = con.cursor()
cur.execute('select l.id, l.contrato.id from lista_contratos l')
for result in cur:
    print result
cur.close()
con.close()