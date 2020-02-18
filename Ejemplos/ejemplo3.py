import cx_Oracle

con = cx_Oracle.connect('HR/HR@127.0.0.1')
cur = con.cursor()
cur.execute('select TABLE_NAME, c.COL_INFO.name c1, c.COL_INFO.data_type c2, c.COL_INFO.data_length c3 from V_COL_INFO c')
for res in cur:
    print (res)
cur.close()
con.close()