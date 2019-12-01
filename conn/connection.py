import cx_Oracle
conn = cx_Oracle.connect('pf','pf','XE')

print(conn.version)