import pymysql  as MySQLdb
from mysql.connector import connect, Error
from pymysql.cursors import Cursor
from config import *

ob = Conecta()
h = ob.Host()
u = ob.User()
pas = ob.Passwd()
bd = ob.bd()

def conectaDb():
    
    db = MySQLdb.connect(host=h, 
                        port=3306, 
                        user=u, 
                        password=pas, 
                        db=bd,read_timeout=30,write_timeout=30,connect_timeout=30)

    return db


def procesa(cursor, sql, *args ):

    success = 0
    out = ""
    db = conectaDb()
    cursor = db.cursor()

    cursor.execute( sql,args  )
    rows = cursor.fetchall()

    for row in rows:
        #print(row )
        out = row

    return out
 
    


rut = "11111111-1"
SQL = "SELECT nombres_apellidos from gente where rut= %s"

cursor = conectaDb()
ok = procesa(cursor , SQL,rut )

print( ok)
