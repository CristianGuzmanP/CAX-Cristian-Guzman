#comentarios son lineas que no se ejecutan y son de uso del programador

#aqui modifique algo
#print('hola')

'''print('hola')
print('hola')
print('hola')
print('hola')
print('hola')
print('hola')
print('hola')'''

'''#constantes tiene informacion que no cambia

pie=3.1416

#variables por que la informacion que contiene PUEDE cambiar


fecha=7
fecha=8
########### ejemplo de una linea que no quiero usar ahorita#######
#while True:
#  fecha=fecha+1


#tipos de Datos

#INT o integers o enteros

entero=456

#FLOAT O floating o flotantes

flotantes=456.5

#string o cadenas

ejemplo1="hola que hace"
ejemplo2='nada tomo clase'
ejemplo3="123456789 y letras hdsufhuhsukghfjukgewukfg"

#bool o boolean o booleanos estos evaluan un falso o verdadero

aprobado=True
reprobartodogrupo=False

#comandos

#print(mensaje): es mandar a la CONSOLA informacion del codigo

#print para imprimir datos ya guardados en variable/const
print(ejemplo1)
print(aprobado)
print(ejemplo3)
print(fecha)

print(ejemplo1, aprobado, ejemplo3, fecha)

#print para imprimir directamente
print('hola k ace')
print('123456789')

#print combinado

print('el mensaje fue: ', ejemplo1)
print(fecha, ' de enero')
print('primer mensaje' , ejemplo1, ' segundo mensaje ', ejemplo2)

#input() permite que el USUARIO ingrese informacion al CODIGO, el codigo no avanza hasta que detecte un error del teclado


nombre=input('ingrese su nombre ')
print('hola ', nombre)

apellido=input('ingrese su apellido ')
print('su nombre completo es ', nombre, apellido)

#SOLO INGRESA CADENAS (STRINGS)

num=input('ingrese numero ')
print('el numero 10 veces es: ',(10*num))

#int() sirve para convertir una STRING en un INT
#float() sirve para convertir una STRING en un Floating
num2=int(input('ingrese numero '))
print('el numero 10 veces es: ',(10*num2))


#while() es una estructura que permite repetir un codigo practicamente de manera infinita

#evaluacion para falso o verdadero

while True:
  print('hola')'''

#comparadores

# == identico
# >< mayor o menos
# != diferente
# >= <= mayor o igual   menor o igual



zeta=int(input('numero: '))

while (zeta>=5):
  print('tu numero es mayor o igual que 5')


pasw=input('password: ')
while (pasw!='hola'):
  print('volver a intentar')