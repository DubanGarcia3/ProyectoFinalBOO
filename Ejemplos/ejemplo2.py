from cy_Oracle import OracleDB

myDB = OracleDB(user='HR', password='HR', databaseURL='127.0.0.1/XE')
con = myDB.connect()
cur = con.cursor()

cur.execute('''create or replace type T_COL_INFO as object(
    NAME        varchar2(85 char),
    DATA_TYPE   varchar2(106 char),
    DATA_LENGTH number,
    COMMENTS    varchar2(4000 char))
    ''')

cur.execute('''create or replace view V_COL_INFO as
            SELECT C.TABLE_NAME AS TABLE_NAME,
            T_COL_INFO(C.COLUMN_NAME,C.DATA_TYPE,C.DATA_LENGTH, M.COMMENTS) AS COL_INFO
                FROM USER_TAB_COLUMNS C, USER_COL_COMMENTS M
                WHERE C.COLUMN_NAME = M.COLUMN_NAME AND C.TABLE_NAME = M.TABLE_NAME
                ''')

for row in cur.execute('select TABLE_NAME, c.COL_INFO.name c1, c.COL_INFO.data_type c2, c.COL_INFO.data_length c3 from V_COL_INFO c'):
    print ('Tabla:%s -- %s -- %s -- %s' % (row.table_name, row.c1, row.c2, row.c3))
cur.close()
con.close()