import cx_Oracle
conn = cx_Oracle.connect('hr','hr','XE')

print(conn.version)