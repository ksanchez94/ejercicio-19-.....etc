#Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
#Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
#Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
#Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.

from calendar import c
from distutils import ccompiler
from distutils.errors import CCompilerError
import email
from tty import CC


alfabeto="abcdefghijklmnñopqrstuvwxyz"
corrimient=int(input("Corrimient: "))
for i in range(5):
    mensaje=input("Mensaje a encriptar: ")
    encriptad=""
    for caracter in mensaje:
        if caracter.lower() in alfabeto:
            indice=alfabeto.find(caracter.lower())
            indice=(indice+corrimient)%27
            encriptad+=alfabeto[indice]
        else:
            encriptad+=caracter
        print("Mensaje encriptad: ", encriptad)
        
def usuarioalingresar():
#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
anioInicio: int(input("Año Inicial:"))
aniofinal=int(input("Año Final:"))
for anio in range(anioInicio, aniofinal+1):
    if not anio%10==0:
        continue
    if not anio%4==0:
        continue
    if anio%100!=0 or anio%400==0:
        print(anio)


    
def validaremail():
 #Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

    caracterBuscado="@"
    emailValido=False
    for c in email: False
        if ccompiler.CCompiler==(caracterBuscado): 
            return True
    return False

#programa principal
direccion=input("Tu email: ")
if ("direccion"):
    print("Dirección válida")
else:
    print("Dirección inválida")
    
def dumaDigitos(numero):
#Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).

    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

#programa principal
sumatoria=0
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:","sumaDigitos"(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", "sumadedigitos:", "Sumatoria:")

#Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

def primo(num):
   for i in range(2,num):
    if num%i==0:           
        return False
    return True

#programa principal
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")
    
#Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

#programa principal
cantidad=0
numero=int(input("Número (-1 para cortar): "))
while numero!=-1:
    print("Factorial:", factorial(numero))
    cantidad+=1
    numero=int(input("Número (-1 para cortar): "))
print("Se leyeron",cantidad,"números")

#Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#programa principal
cantidad=0
mayor=-1
numero=int(input("Número positivo: "))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma > mayor:
          mayor=suma
          n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input("Número positivo: "))
print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
print("Cantidad con sumatoria menor a 10:",cantidad)

#El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?

def maximo(a,b):
  if x>y:
    return x
  else:
    return y

def minimo(a,b):
  if x<y:
    return x
  else:
    return y

#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

#Sin ejecutar el siguiente programa, determinar cuál es la salida en pantalla si se ingresan los valores x=6, y=7:

def coordenadaZ(x,y):
  x=x+10
  y=y+15
  return x+y

#programa principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
  z=coordenadaZ(x,y)
  x=x+1
  y=y+1
print(x," . ",y)

#Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

def lenUltimaPalabra(frase):
   if len(frase)==0:
       return 0
   cantidad=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cantidad+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad=0
   return cantidad

 #Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def validarDNI(dni):
   cantidad=0
   while dni!=0:
       cantidad+=1
       dni//=10
   return cantidad==7 or cantidad==8

#Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

def lenUltimaPalabra(frase):
    if len(frase)==0:
        return
    cantidad=0
    for i in range(len(frase)):
        if frase[i]!=' ':
            cantidad+=1
        else:
            if i<len(frase)-1 and frase[i+1]!=' ':
                cantidad=0

#Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.
#Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido, el usuario sólo ingresará uno.
#Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
#Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
#Nombre: Alba María Linares
#DNI: 25834910
#Alba7258

def lenUltimaPalabra(cadena):
   longitud=len(cadena)
   if longitud==0:
       return 0
   cantidad=0
   for i in range(longitud):
       if cadena[i]!=' ':
           cantidad+=1
       else:
           if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
               cantidad=0
   return cantidad

def DNIvalido(dni):
   cantidad=0
   while dni!=0:
       cantidad+=1
       dni//=10
   return cantidad==7 or cantidad==8

def primerosTresDigitos(numero):
   while numero >= 1000:
     numero = numero // 10
   return numero

def obtenerIdentificador(nombre, dni):
   nombre=nombre.strip()
   id=nombre[:nombre.find(" ")]
   id=id+str(lenUltimaPalabra(nombre))
   id=id+str(primerosTresDigitos(dni))
   return id

#programa principal
nombre=input("Nombre del socio: ")
while nombre!="":
   dni=int(input("DNI del socio: "))
   while(DNIvalido(dni)):
      print("Número inválido.")
      dni=int(input("DNI del socio: "))
   print(obtenerIdentificador(nombre,dni))
   nombre=input("Nombre del socio: ")
   
   