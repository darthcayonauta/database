from lxml import etree

class Params:
    s=""
    u=""
    c=""
    d=""

    def __init__(self):
        doc = etree.parse("config.xml")
        keys= doc.findall("section")
        self.s = keys[0].find("data").text
        self.u = keys[1].find("data").text
        self.c = keys[2].find("data").text
        self.d = keys[3].find("data").text 

    def sx(self):
        return self.s
    
    def ux(self):
        return self.u
    
    def cx(self):
        return self.c

    def dx(self):
        return self.d  