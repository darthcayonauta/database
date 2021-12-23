import pymysql  as MySQLdb
from mysql.connector import connect, Error
from pymysql.cursors import Cursor
from config import *

class PruebaConexion:
    #atributos
    servidor = ""
    usuario  = ""
    clave    = ""
    puerto   = ""
    Db       = ""

    #constructor
    def __init__(self):
         ob_conecta = Conecta()
         self.servidor = ob_conecta.Host()
         self.usuario = ob_conecta.User()
         self.clave = ob_conecta.Passwd()
         self.puerto = ob_conecta.Port()
         self.Db = ob_conecta.bd()

    def conectaDb(self):
          db = MySQLdb.connect(host=self.servidor, 
                        port=self.puerto, 
                        user=self.usuario, 
                        password=self.clave, 
                        db=self.Db,read_timeout=30,write_timeout=30,connect_timeout=30)

          return db   

    def ejecutaQuery(self,query,*args):

        #print( query,args )

        out =""
        db = self.conectaDb()
        cursor = db.cursor()
        cursor.execute( query,args )

        rows = cursor.fetchall()

        for row in rows:
            out = row

        return out        

    def insertUpdate(self,query,*args):
        db = self.conectaDb()
        cursor = db.cursor()
        cursor.execute(query,args)
        db.commit()

        return "Accion Realizada para esta consulta" 


    def cierra(self):
        db = self.conectaDb()
        db.close()
