from cy_Oracle import OracleDB
from cy_Oracle import Attribute

class ColInfo(object):
    def __init__(self):
        self.name=None
        self.oracleDataType=None
        self.oracleDataLenght=None
        
    def __str__(self):
        return 'name=%s type=%s(%d)' % \
            (self.name,self.oracleDataType,self.oracleDataLenght)
            
            
myDB = OracleDB(user='HR', password='HR', databaseURL='127.0.0.1')
con = myDB.connect()
cur = con.cursor()

cur.execute('''create or replace type T_COL_INFO as object(
    NAME        varchar2(85 char),
    DATA_TYPE   varchar2(106 char),
    DATA_LENGTH number,
    COMMENTS    varchar2(4000 char))
    ''')

cur.execute('''create or replace view V_COL_INFO as
            SELECT C.TABLE_NAME AS TABLE_NAME, T_COL_INFO(
                C.COLUMN_NAME,C.DATA_TYPE,C.DATA_LENGTH, M.COMMENTS) AS COL_INFO
                FROM USER_TAB_COLUMNS C, USER_COL_COMMENTS M
                WHERE C.COLUMN_NAME = M.COLUMN_NAME AND C.TABLE_NAME = M.TABLE_NAME''')

myDB.addTypemap(oracleTypename='T_COL_INFO', pythonClass=ColInfo, attrDict={
    'name'              : Attribute('NAME'),
    'oracleDataType'    : Attribute('DATA_TYPE'),
    'oracleDataLenght'  : Attribute('DATA_LENGTH'),
    })

for row in cur.execute('SELECT TABLE_NAME, COL_INFO FROM V_COL_INFO'):
    print ('Table::%s "%s"::%s' % (row.table_name,row.col_info.__class__.__name__,row.col_info))
cur.close()
con.close()