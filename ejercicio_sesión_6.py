# -*- coding: utf-8 -*-
"""Ejercicio Sesión 6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iu5v0MOKcUA_wDM7o3yOhMAPBIk8fOUX
"""

#variable
x = 25
X = -23
edad = 40
var = 4.50
notas =5.0
variable_texto = "Juan"
Variable_1 = "Gomez"
Frase = "La vida es bella"
verdad = True
Falso = False
print(x)
print(X)
print(edad)
print(var)
print(notas)
print(variable_texto)
print(Variable_1)
print(Frase)
print(verdad)
print(Falso)
#Listas
Listas=["Manzana", "Banano", "Fresa"]
print(Listas[0])

"""Tuplas"""

nota = (4.5,3.5)
print(nota[1])

"""Diccionario"""

persona = {"nombre": "Ana", "edad": 30}
print(persona["edad"])

"""Conjuntos"""

x={1,2,3,3}
print(x)

"""Función Type: tipo de dato"""

nombre="Juan"
edad=30
print(type(nombre))
print(type(edad))

"""Función input: dato por teclado"""

nombre=input("Ingrese su nombre: ")
print(nombre)

"""Argumentos
\n salto de linea
END: comportamiento de la función
"""

print("1 de mayo no sé", "trabaja", end="\n")
print("Se descansa", end="----")

"""Argumento SEP"""

print("1 de mayo no sé", "trabaja", sep=" - ")

"""3 funciones print"""

print("La vida es bella")
print()
print("y tenemos sueños que se cumplen")

X=5+2
print(X)

a=10
b=3
z=a//b
print(z)

x=5%2
print(x)

x=10**3
print(x)

x=4
if x>5:
  print("x es mayor que 5")
else:
  print("x es menor que 5")

for x in range(10):
  print(x)

i=0
while i<5:
  print(i)
  i+=1

for i in range(7):
  if i==3:
    continue
  print(i)

for i in range(7):
  if i==3:
    break
  print(i)

numero=int(input("Ingrese un numero: "))
if numero>0:
  print("El numero es positivo")

while True:
  numero=int(input("Ingrese un numero(3 salir):"))
  if numero==5:
    print("Saliste")
    break
  else:
    print("El numero es: ", numero)

# Realizar un programa que recorra la lista de números
for num in range(1, 6): # Números del 1 al 5
  if num == 4:
    print("Número 4 encontrado, deteniendo el bucle.")
    break # Detener el bucle cuando num es 4

  # Uso de condicionales para verificar si es par o impar
  if num % 2 == 0:
    print(f"{num} es par")
  else:
    print(f"{num} es impar")

# Uso de while para contar hasta 3
i = 0
while i < 3:
  print(f"Contando: {i}")
  i += 1