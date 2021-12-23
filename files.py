import cv2
import numpy as np
from classPruebaConexion import *


def write_file( data, filename ):
    with open(filename,'wb') as f:
        f.write(data)


def write_file2(id_user, name,data):
    with open('{}_{}.jpg'.format(name,id_user ), 'wb') as f:
        f.write( data )



#main
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

SQL = "SELECT * FROM archivo WHERE id=%s"
id  = 1

#instancio clases y creo objetos
ob_prueba_conexion = PruebaConexion()
result = ob_prueba_conexion.ejecutaQuery( SQL,id )

myFile = result[2]
fileName = "margarete.jpg"

write_file( myFile, fileName )
write_file2( result[0],result[1],result[2] )

img = cv2.imread( fileName )

#grises
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#DETECTANDO ROSTROS EN ESCALA DE GRISES
faces = face_cascade.detectMultiScale( gray,1.3,5 )

#iterando en cada rostro

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#
    roy_gray = gray[y:y+h,x:x+w]
    roy_color = img[y:y+h,x:x+w]

    #ojos
    eyes = eye_cascade.detectMultiScale( roy_gray )
    #creo los rectangulos en los ojos
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle( roy_color,(ex,ey),(ex+ew, ey+eh), (0,255,0),2 )


#cv2.imshow( result[1],img )
cv2.imshow( result[1],img )
cv2.waitKey( 0 )
cv2.destroyAllWindows()

ob_prueba_conexion.cierra()

