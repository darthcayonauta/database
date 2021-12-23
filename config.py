from xmlp1 import *

class Conecta:

    ob_param = Params()

    host   = ob_param.sx()
    port   = 3306 
    user   = ob_param.ux()
    passwd = ob_param.cx()
    db     = ob_param.dx()


    def Host(self):
        return self.host

    def User(self):
        return self.user

    def Passwd(self):
        return self.passwd

    def Port(self):
        return self.port

    def bd(self):
        return self.db    
