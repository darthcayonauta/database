import  io
import  matplotlib.pyplot as plt 
from PIL import Image
from classPruebaConexion import *

SQL = "SELECT * FROM archivo WHERE id=%s"
id  = 2

#instancio clases y creo objetos
ob_prueba_conexion = PruebaConexion()
result = ob_prueba_conexion.ejecutaQuery( SQL,id )

data = result[2]


print("leyendo imagen.....")

#reading file
with open("margarete.jpg", "rb") as f:
  image_bytes = f.read()


#im = plt.imread(io.BytesIO(image_bytes))
im = plt.imread('margarete.jpg')
image = Image.open('margarete.jpg')
image2 = Image.open( io.BytesIO( data ) )

plt.imshow(image2)
plt.show()


#print( image_bytes )