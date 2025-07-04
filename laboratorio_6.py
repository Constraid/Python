# -*- coding: utf-8 -*-
"""Laboratorio 6

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q_QpHIByWoYadeSJY_TUDvy7E8qs1ROR

1.	Algoritmo para Preparar un Té: Este algoritmo describe los pasos para preparar un té y lo implementamos en Python.

-	Pasos:
Calentar Agua
Colocar una bolsa de té en la taza
Poner agua caliente en la taza
Esperar tiempo definido para él té
Retirar la bolsa de té y beber
"""

agua_caliente = True
bolsa_te = True

if agua_caliente and bolsa_te:
	print ("Colocar una bolsa de té en la taza")
	print ("Poner agua caliente en la taza")
	print ("Esperar tiempo definido para él té")
	print ("Retirar la bolsa de té y beber")
else:
	print ("No puedes preparar el té porque falta agua caliente o bolsa de té")

"""2.	Cálculo del Promedio de Notas: Utilizar variables y tipos de datos para almacenar las notas de un estudiante, y un operador aritmético para calcular el promedio.

-	Pasos:
recopilo las notas a calcular en variables
defino formula de promedio P=Suma de las notas/la cantidad total de notas
muestro el resultado en pantalla


"""

#Variables para almacenar las notas
nota1 = 4.7
nota2 = 3.2
nota3 = 2.5

# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Mostrar el promedio
print("El promedio del estudiante es:", promedio)

"""3.	Verificar si un Número es Par o Impar: Utiliza condicionales para verificar si un número es par o impar, y operadores para realizar el cálculo.
-	Pasos:
solicitar número a ser revisado
para verificar si es par se divide por 2 y si su residuo es 0 entonces es par
sino es impar

"""

#Solicitar el numero al usuario
numero = int(input("Ingrese un numero: "))
#Varificar si es par o impar
if numero % 2 == 0:
  print("El numero es par")
else:
  print("El numero es impar")

"""4.	Bucle for para Imprimir Números del 1 al 5: Usar un bucle for para mostrar los números del 1 al 5 y combinar los operadores aritméticos para mostrar si son pares o impares.

-	Pasos:
defino mi ciclo y hasta donde va
con condicionales defino o calculo si son pares o impares
y imprimo en cada revisión


"""

#Usar un bucle for para recorrer numeros y decir si son pares o impares
for num in range(1, 10):
#Varificar si es par o impar
  if num % 2 == 0:
    print(f"{num} es par")
  else:
    print(f"{num} es impar")

"""5.	Convertir Grados Celsius a Fahrenheit: Usar una función para convertir grados Celsius a Fahrenheit. La fórmula para la conversión es Fahrenheit = (Celsius * 9/5) + 32.
-	Pasos:
definir la función para convertir
Solicitar la temperatura en grados centígrados al usuario
Calcular y devolver la temperatura convertida

"""

# Definir la función para convertir de Celsius a Farenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicitar la temperarura en celsius al usuario
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Calcular y mostrar la temperatura en Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")

"""6.	Contar la Cantidad de Vocales en una Cadena de Texto: Utilizar un bucle for y una condicional para contar cuántas vocales hay en una cadena de texto ingresada por el usuario.

-	Pasos:
solicitar una cadena de texto al usuario
Crear un contador de vocales
recorrer la cadena con el bucle for y verificar si el carácter es una vocal
mostrar el total de vocales encontradas

"""

#Solicitar una cadena de texto
texto = input("Ingrese una frase: ")

#Crear un contador de vocales
contador_vocales = 0

#Recorrer la cadena con el bucle for y verificar si el carácter es una vocal
for letra in texto:
    if letra.lower() in "aeiou":
        contador_vocales += 1

#Mostrar el total de vocales encontradas
print(f"En la frase hay {contador_vocales} vocales.")

"""7.	Calcular el Factorial de un Número: Usar un bucle while para calcular el factorial de un número ingresado por el usuario. El factorial de un número n (n!) es el producto de todos los números enteros positivos menores o iguales a n.
-	Pasos:
solicitar un numero al usuario
inicializar el resultado en 1
utilizar el bucle while para multiplicar los numero hasta llegar a 1
imprimir resultado

"""

#solicitar un numero al usuario
numero = int(input("Ingrese un numero: "))

#inicializar el resultado en 1
factorial = 1

#Calcular el factorial usando un bucle while
while numero > 0:
    factorial *= numero
    numero -= 1

#Imprimir el resultado
print(f"El factorial de {numero} es {factorial}.")